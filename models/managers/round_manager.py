from models.entities.match import Match
from models.entities.round import Round
from models.managers.player_manager import PlayerManager


class RoundManager:
    def __init__(self):
        self.player_manager = PlayerManager()

    def round_to_dict(self, round):
        if isinstance(round, Round):
            return {
                "round_id": round.round_id,
                "name": round.name,
                "matches": [self.match_to_dict(match) for match in round.matches],
                "start_date": round.start_date,
                "end_date": round.end_date
            }
        elif isinstance(round, dict):
            return self.round_from_dict(round)
        else:
            raise TypeError("Expected Round object or dictionary")

    def match_to_dict(self, match):
        return {
            "name": match.name,
            "player1": match.player1.player_id,
            "player2": match.player2.player_id,
            "score1": match.score1,
            "score2": match.score2,
            "winner": match.winner.player_id if match.winner else None
        }

    def round_from_dict(self, data):
        round = Round(data["name"])
        round.round_id = data["round_id"]
        round.start_date = data.get("start_date", None)
        round.end_date = data.get("end_date", None)

        round.matches = [
            Match(
                name=match_data["name"],
                round=round,
                player1=self.player_manager.get_player(match_data["player1"]),
                player2=self.player_manager.get_player(match_data["player2"]),
                score1=match_data["score1"],
                score2=match_data["score2"],
                winner=self.player_manager.get_player(match_data["winner"]) if match_data["winner"] else None
            )
            for match_data in data["matches"]
        ]
        return round
