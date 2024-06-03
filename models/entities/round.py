import uuid


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = None
        self.end_date = None
        self.matches = []
        self.round_id = str(uuid.uuid4().hex[:5])

    def add_match(self, match):
        self.matches.append(match)

    def is_finished(self):
        return all(match.is_finished() for match in self.matches)

    def get_report(self):
        report = f"  {
        self.name} - Start: {self.start_date}, End: {self.end_date}\n"
        for match in self.matches:
            report += f"    - {match}\n"
        return report

    def __str__(self):
        return f"Round {self.name} - Start: {self.start_date}, End: {self.end_date}"
