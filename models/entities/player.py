class Player:
    def __init__(self, last_name, first_name, birthdate, player_id=None, total_points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id
        self.total_points = total_points

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.player_id == other.player_id
        return False

    def __hash__(self):
        return hash(self.player_id)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.name} ({self.player_id}), born {self.birthdate}, total points: {self.total_points}"
