import os

from models.managers.player_manager import PlayerManager
from models.managers.tournament_manager import TournamentManager
from views.main_view import MainView
from views.reports_view import ReportsView
from views.tournament_view import TournamentView


class ReportsController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.reports_folder = "reports"
        os.makedirs(self.reports_folder, exist_ok=True)

    def reports_menu(self):
        while True:
            choice = ReportsView.generate_reports_menu()
            match choice:
                case "1":
                    self.report_all_players_alphabetical()
                case "2":
                    self.report_all_tournaments()
                case "3":
                    self.report_tournament_details()
                case "4":
                    self.report_tournament_players_alphabetical()
                case "5":
                    self.report_tournament_rounds_and_matches()
                case "b":
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue
            break

    def report_all_players_alphabetical(self):
        """Generates a report of all players sorted alphabetically by last name."""
        players = self.player_manager.get_all_players()
        if not players:
            MainView.print_error_action("No players found.")
            return

        players.sort(key=lambda p: p.last_name.lower())
        report_content = "\n--- All Players (Alphabetical Order) ---\n"
        for player in players:
            report_content += f"- {player.last_name} {player.first_name} ({player.player_id})\n"

        self.save_report("all_players_alphabetical.txt", report_content)

    def report_all_tournaments(self):
        """Generates a report listing all tournaments."""
        tournaments = self.tournament_manager.load_tournaments_from_json()
        if not tournaments:
            MainView.print_error_action("No tournaments found.")
            return

        report_content = "\n--- All Tournaments ---\n"
        for tournament in tournaments:
            report_content += f"- {tournament}\n"

        self.save_report("all_tournaments.txt", report_content)

    def report_tournament_details(self):
        """Generates a report with name and dates for a specific tournament."""
        tournament_name = TournamentView.get_tournament_selection()
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_error_action(f"Tournament '{tournament_name}' not found.")
            return

        report_content = "\n--- Tournament Details ---\n"
        report_content += f"Name: {tournament.name}\n"
        report_content += f"Location: {tournament.location}\n"
        report_content += f"Start Date: {tournament.start_date}\n"
        report_content += f"End Date: {tournament.end_date}\n"

        self.save_report(f"tournament_details_{tournament_name}.txt", report_content)

    def report_tournament_players_alphabetical(self):
        """Generates a report listing players in a tournament alphabetically."""
        tournament_name = TournamentView.get_tournament_selection()
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_error_action(f"Tournament '{tournament_name}' not found.")
            return

        players = tournament.registered_players
        if not players:
            MainView.print_error_action(f"No players found in tournament '{tournament_name}'.")
            return

        players.sort(key=lambda p: p.last_name.lower())
        report_content = f"\n--- Players in Tournament'{tournament.name}' (Alphabetical Order) ---\n"
        for player in players:
            report_content += f"- {player.last_name} {player.first_name} ({player.player_id})\n"

        self.save_report(f"tournament_players_{tournament_name}.txt", report_content)

    def report_tournament_rounds_and_matches(self):
        """Generates a report listing all rounds and matches in a tournament."""
        tournament_name = TournamentView.get_tournament_selection()
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_error_action(f"Tournament '{tournament_name}' not found.")
            return

        report_content = f"\n--- Rounds and Matches in the Tournament'{tournament.name}' ---\n\n"
        for i, round in enumerate(tournament.rounds):
            report_content += f"{round.name}, Start: {round.start_date}, End: {round.end_date} \n"
            for j, match in enumerate(round.matches):
                report_content += f"  Match {j + 1}: {match}\n\n"

        self.save_report(f"tournament_rounds_and_matches_{tournament_name}.txt", report_content)

    def save_report(self, filename, content):
        """Saves the given content to a report file in the reports folder."""
        with open(os.path.join(self.reports_folder, filename), 'w') as file:
            file.write(content)
        MainView.print_success_action(f"Report saved as {filename}")
