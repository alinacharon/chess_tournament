import uuid


class Tournament:
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.registered_players = []
        self.rounds = []
        self.notes = ""
        self.rounds_num = 0
        self.past_matches = set()
        self.tournament_id = str(uuid.uuid4().hex[:5] )

    def __str__(self):
        return (f"{self.name} ({self.location}), Start date: {self.start_date},"
                f" End date: {self.end_date}")
