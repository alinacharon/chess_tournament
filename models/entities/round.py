import uuid


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None
        self.matches = []
        self.round_id = str(uuid.uuid4().hex[:5])

    def __str__(self):
        return f"Round {self.name} - Start: {self.start_date}, End: {self.end_date}"
