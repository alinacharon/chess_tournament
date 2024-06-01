import json
import os

from models.entities.tournament import Tournament
from models.managers.player_manager import PlayerManager



class TournamentManager:
    def __init__(self):
        self.data_folder = "data"
        os.makedirs(self.data_folder, exist_ok=True)
        self.tournaments_file = os.path.join(self.data_folder, "tournaments.json")
        self.tournaments = []
        self.player_manager = PlayerManager()

    def save_tournament(self, tournament):
        data_for_db = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "tournament_id": tournament.tournament_id,
            "registered_players": [player.player_id for player in tournament.registered_players],
            "rounds": [self.round_to_dict(round) for round in tournament.rounds]
        }
        self.write_in_db(data_for_db)

    def write_in_db(self, data_for_db):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                data = json.load(file)
        else:
            data = []
        for i, tournament in enumerate(data):
            if tournament["name"] == data_for_db["name"]:
                data[i] = data_for_db
                break
        else:
            data.append(data_for_db)
        with open(self.tournaments_file, "w") as file:
            json.dump(data, file, indent=4)

    def pull_data_for_tournament(self, tournament_name):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                data = json.load(file)
            for tournament in data:
                if tournament["name"] == tournament_name:
                    return tournament
        return None

    def get_all_tournaments(self):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                tournaments_data = json.load(file)
            tournaments = []
            for tournament_data in tournaments_data:
                tournament = Tournament(
                    tournament_data["name"],
                    tournament_data["location"],
                    tournament_data["start_date"],
                    tournament_data["end_date"],
                )
                tournament.registered_players = [
                    self.player_manager.get_player(player_id)
                    for player_id in tournament_data.get("registered_players", [])
                ]
                tournaments.append(tournament)
            return tournaments
        else:
            return []

    def get_tournament(self, tournament_name):
        data = self.pull_data_for_tournament(tournament_name)
        if data:
            tournament = Tournament(
                name=data["name"],
                location=data["location"],
                start_date=data["start_date"],
                end_date=data["end_date"]
            )
            tournament.registered_players = [
                self.player_manager.get_player(player_id) for player_id in data.get("registered_players", [])
            ]
            return tournament
        else:
            return None
