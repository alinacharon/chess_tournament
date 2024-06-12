from models.managers.player_manager import PlayerManager
from models.managers.tournament_manager import TournamentManager
from views.main_view import MainView
from views.reports_view import ReportsView


class ReportsController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()

    def reports_menu(self):
        choice = ReportsView.generate_reports_menu()
        while True:
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
                    MainView.main_menu()
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
            print("No players found.")
            return

        players.sort(key=lambda p: p.last_name.lower())
        MainView.print_info("\n--- All Players (Alphabetical Order) ---\n")
        for player in players:
            MainView.print_info(f"- {player.last_name} {player.first_name}  ({player.player_id})")

    def report_all_tournaments(self):
        """Generates a report listing all tournaments."""
        tournaments = self.tournament_manager.load_tournaments_from_json()
        if not tournaments:
            MainView.print_error_action("No tournaments found.")
            return

        MainView.print_info("\n--- All Tournaments ---\n")
        for tournament in tournaments:
            MainView.print_info(f"- {tournament.name}")

    def report_tournament_details(self):
        """Generates a report with name and dates for a specific tournament."""
        tournament_name = input("Enter tournament name: ")
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_info(f"Tournament '{tournament_name}' not found.")
            return

        MainView.print_info("\n--- Tournament Details ---\n")
        MainView.print_info(f"Name: {tournament.name}")
        MainView.print_info(f"Location: {tournament.location}")
        MainView.print_info(f"Start Date: {tournament.start_date}")
        MainView.print_info(f"End Date: {tournament.end_date}")

    def report_tournament_players_alphabetical(self):
        """Generates a report listing players in a tournament alphabetically."""
        tournament_name = input("Enter tournament name: ")
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_error_action(f"Tournament '{tournament_name}' not found.")
            return

        players = tournament.registered_players
        if not players:
            MainView.print_error_action(f"No players found in tournament '{tournament_name}'.")
            return

        players.sort(key=lambda p: p.last_name.lower())
        MainView.print_info(f"\n--- Players in '{tournament.name}' (Alphabetical Order) ---\n")
        for player in players:
            MainView.print_info(f"- {player.last_name} {player.first_name} ({player.player_id})")

    def report_tournament_rounds_and_matches(self):
        """Generates a report listing all rounds and matches in a tournament."""
        tournament_name = input("Enter tournament name: ")
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_error_action(f"Tournament '{tournament_name}' not found.")
            return

        MainView.print_info(f"\n--- Rounds and Matches in '{tournament.name}' ---\n")
        for i, round in enumerate(tournament.rounds):
            MainView.print_info(f"{round.name}")
            for j, match in enumerate(round.matches):
                player1 = self.player_manager.get_player(match.player1.player_id)
                player2 = self.player_manager.get_player(match.player2.player_id)

                player1_name = f"{player1.first_name} {player1.last_name}" if player1 else "Unknown"
                player2_name = f"{player2.first_name} {player2.last_name}" if player2 else "Unknown"

                MainView.print_info(f"  Match {j + 1}: {player1_name} vs {player2_name}")
