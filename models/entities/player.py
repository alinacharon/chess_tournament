class Player:
    def __init__(self, last_name, first_name, birthdate, player_id=None):
        self.last_name = last_name
        self._first_name = first_name
        self.birthdate = birthdate
        self.player_id = player_id
        self.total_points = 0

    @property
    def first_name(self):
        return self._first_name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.name} ({self.player_id}), born {self.birthdate}, Points: {self.total_points}"


