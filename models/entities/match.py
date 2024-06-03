import uuid


class Match:
    def __init__(self, name, player1, player2, score1=0, score2=0, winner=None, match_id=None):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.winner = winner
        self.match_id = match_id or str(uuid.uuid4().hex[:5])

    def set_result(self, winner):
        if winner == self.player1:
            self.winner = winner
            self.score1 = 1
        elif winner == self.player2:
            self.winner = winner
            self.score2 = 1
        else:
            self.winner = "Draw match"
            self.score1 = 0.5
            self.score2 = 0.5

    def is_finished(self):
        return self.winner is not None

    def __str__(self):
        if self.winner is None:
            return f"{self.player1.name} ({self.score1}) vs. {self.player2.name} ({self.score2}) - Not finished"
        elif self.winner == "Draw match":
            return f"{self.player1.name} ({self.score1}) vs. {self.player2.name} ({self.score2}) - Draw"
        else:
            return (f"{self.player1.name} ({self.score1}) vs. {self.player2.name} "
                    f"({self.score2}) - Winner: {self.winner.player.name}")
