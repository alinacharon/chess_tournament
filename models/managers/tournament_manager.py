import json
import os

from models.entities.tournament import Tournament


class TournamentManager:
    def __init__(self):
        self.data_folder = "data"
        os.makedirs(self.data_folder, exist_ok=True)
        self.tournaments_file = os.path.join(self.data_folder, "tournaments.json")

    def save_tournament(self, tournament):
        data_for_db = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "tournament_id": tournament.tournament_id
        }
        self.write_in_db(data_for_db)

    def write_in_db(self, data_for_db):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                data = json.load(file)

        else:
            data = []

        for i, tournament in enumerate(data):
            if tournament["tournament_id"] == data_for_db["tournament_id"]:
                data[i] = data_for_db
                break

        else:
            data.append(data_for_db)
        with open(self.tournaments_file, "w") as file:
            json.dump(data, file, indent=4)

    def pull_data_for_tournament_by_id(self, tournament_id):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                data = json.load(file)
            for tournament in data:
                if tournament["tournament_id"] == tournament_id:
                    return tournament
        return None

    def get_tournament(self, tournament_id):
        data = self.pull_data_for_tournament_by_id(tournament_id)
        if data:
            return Tournament(
                name=data["name"],
                location=data["location"],
                start_date=data["start_date"],
                end_date=data["end_date"])

        else:
            return None

    def get_all_tournaments(self):
        if os.path.exists(self.tournaments_file):
            with open(self.tournaments_file, "r") as file:
                data = json.load(file)
            return [Tournament(
                name=tournament_data["name"],
                location=tournament_data["location"],
                start_date=tournament_data["start_date"],
                end_date=tournament_data["end_date"]) for tournament_data in data]
        else:
            return []
