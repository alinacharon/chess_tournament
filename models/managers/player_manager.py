import json
import os

from models.entities.player import Player


class PlayerManager:
    def __init__(self):
        self.data_folder = "data"
        os.makedirs(self.data_folder, exist_ok=True)
        self.players_file = os.path.join(self.data_folder, "players.json")
        self.players = self.load_players_from_json()

    def load_json_file(self):
        if os.path.exists(self.players_file):
            with open(self.players_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_json_file(self, data):
        with open(self.players_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_players_from_json(self):
        players_data = self.load_json_file()
        players = []
        for player_data in players_data:
            player = Player(
                last_name=player_data["last_name"],
                first_name=player_data["first_name"],
                birthdate=player_data["birthdate"],
                player_id=player_data["player_id"],
                total_points=player_data.get("total_points", 0)
            )
            players.append(player)
        return players

    def write_in_db(self, player):
        data = self.load_json_file()
        data_for_db = {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "birthdate": player.birthdate,
            "player_id": player.player_id,
            "total_points": player.total_points,
        }

        for i, player_data in enumerate(data):
            if player_data["player_id"] == data_for_db["player_id"]:
                data[i] = data_for_db
                break
        else:
            data.append(data_for_db)

        self.save_json_file(data)

    def pull_data_for_player_by_id(self, player_id):
        data = self.load_json_file()
        for player_data in data:
            if player_data["player_id"] == player_id:
                return player_data
        return None

    def get_player(self, player_id):
        data = self.pull_data_for_player_by_id(player_id)
        if data:
            player = Player(
                last_name=data["last_name"],
                first_name=data["first_name"],
                birthdate=data["birthdate"],
                player_id=data["player_id"],
                total_points=data.get("total_points", 0)
            )
            return player
        else:
            return None

    def get_all_players(self):
        data = self.load_json_file()
        players = [Player(
            last_name=player_data["last_name"],
            first_name=player_data["first_name"],
            birthdate=player_data["birthdate"],
            player_id=player_data["player_id"],
            total_points=player_data.get("total_points", 0)
        ) for player_data in data]
        return players
