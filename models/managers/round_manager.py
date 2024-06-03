from models.entities.match import Match
from models.entities.round import Round
from models.managers.player_manager import PlayerManager


class RoundManager:
    def __init__(self):
        self.player_manager = PlayerManager()

    def round_to_dict(self, round):
        return {
            "round_id": round.round_id,
            "name": round.name,
            "matches": [
                {
                    "match_id": match.match_id,
                    "name": match.name,
                    "player1": match.player1.player_id,
                    "player2": match.player2.player_id,
                    "score1": match.score1,
                    "score2": match.score2,
                    "winner": match.winner.player_id if match.winner else None
                }
                for match in round.matches
            ],
            "start_date": round.start_date,
            "end_date": round.end_date
        }

    def dict_to_round(self, data):
        round = Round("round_name")
        round.name = data["name"],
        round.start_date = data.get("start_date", None),
        round.end_date = data.get("end_date", None),
        round.round_id = data["round_id"]

        round.matches = [
            Match(
                name=match_data["name"],
                player1=self.player_manager.get_player(match_data["player1"]),
                player2=self.player_manager.get_player(match_data["player2"]),
                score1=match_data["score1"],
                score2=match_data["score2"],
                winner=self.player_manager.get_player(match_data["winner"]) if match_data["winner"] else None
            )
            for match_data in data["matches"]
        ]
        return round
