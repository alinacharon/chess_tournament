import json
import os
import uuid

from models.entities.tournament import Tournament
from models.managers.player_manager import PlayerManager
from models.managers.round_manager import RoundManager


class TournamentManager:
    def __init__(self):
        self.data_folder = "data"
        os.makedirs(self.data_folder, exist_ok=True)
        self.tournaments_file = os.path.join(self.data_folder, "tournaments.json")
        self.player_manager = PlayerManager()
        self.round_manager = RoundManager()
        self.tournaments = self.load_tournaments_from_json()

    def load_json_file(self):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_json_file(self, data):
        with open(self.tournaments_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_tournaments_from_json(self):
        tournaments_data = self.load_json_file()
        tournaments = []
        for tournament_data in tournaments_data:
            tournament = Tournament(
                tournament_data["name"],
                tournament_data["location"],
                tournament_data["start_date"],
                tournament_data["end_date"]
            )
            tournament.registered_players = [
                self.player_manager.get_player(player_id)
                for player_id in tournament_data.get("registered_players", [])
            ]
            tournament.rounds = [
                self.round_manager.dict_to_round(round_data)
                for round_data in tournament_data.get("rounds", [])
            ]
            tournament.notes = tournament_data.get("notes", "")
            tournament.rounds_num = tournament_data.get("rounds_num", 0)
            tournament.past_matches = set(tournament_data.get("past_matches", []))
            tournament.tournament_id = tournament_data.get("tournament_id", str(uuid.uuid4().hex[:5]))
            tournaments.append(tournament)
        return tournaments

    def write_in_db(self, tournament):
        data = self.load_json_file()
        data_for_db = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "tournament_id": tournament.tournament_id,
            "registered_players": [player.player_id for player in tournament.registered_players],
            "rounds": [self.round_manager.round_to_dict(round) for round in tournament.rounds],
            "notes": tournament.notes,
            "rounds_num": tournament.rounds_num,
            "past_matches": list(tournament.past_matches)
        }

        for i, tournament_data in enumerate(data):
            if tournament_data["tournament_id"] == data_for_db["tournament_id"]:
                data[i] = data_for_db
                break
        else:
            data.append(data_for_db)

        self.save_json_file(data)

    def pull_data_for_tournament(self, tournament_name):
        data = self.load_json_file()
        for tournament_data in data:
            if tournament_data["name"] == tournament_name:
                return tournament_data
        return None

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
            tournament.rounds = data.get("rounds", [])
            tournament.notes = data.get("notes", "")
            tournament.rounds_num = data.get("rounds_num", 0)
            tournament.past_matches = set(data.get("past_matches", []))
            tournament.tournament_id = data.get("tournament_id", str(uuid.uuid4().hex[:5]))
            return tournament
        return None

    def get_rounds(self, tournament_name):
        tournament_data = self.pull_data_for_tournament(tournament_name)
        if tournament_data:
            return tournament_data.get("rounds", [])
        return []