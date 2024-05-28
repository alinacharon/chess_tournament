import json
import os
from models.entities.player import Player


class PlayerManager:
    def __init__(self):
        self.data_folder = "Data"
        os.makedirs(self.data_folder, exist_ok=True)
        self.players_file = os.path.join(self.data_folder, "players.json")

    def save_player(self, player):
        data_for_db = {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "birthdate": player.birthdate,
            "player_id": player.player_id,
            "total_points": player.total_points,
        }
        self.write_in_db(data_for_db, self.players_file)

    @staticmethod
    def write_in_db(data_for_db, players_file):
        if os.path.exists(players_file):
            with open(players_file, "r") as file:
                data = json.load(file)

        else:
            data = []

        for i, player in enumerate(data):
            if player["player_id"] == data_for_db["player_id"]:
                data[i] = data_for_db
                break

        else:
            data.append(data_for_db)
        with open(players_file, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def pull_data_for_player_by_id(player_id, players_file):
        if os.path.exists(players_file):
            with open(players_file, "r") as file:
                data = json.load(file)
            for player in data:
                if player["player_id"] == player_id:
                    return player
        return None

    def get_player(self, player_id):
        data = self.pull_data_for_player_by_id(player_id, self.players_file)
        if data:
            return Player(
                last_name=data["last_name"],
                first_name=data["first_name"],
                birthdate=data["birthdate"],
                player_id=data["player_id"],
                total_points=data["total_points"],
            )
        else:
            return None
