from models.managers.tournament_manager import TournamentManager
from views.main_view import MainView
from views.tournament_view import TournamentView
from models.entities.tournament import Tournament


class TournamentController:
    def __init__(self):
        self.tournament_manager = TournamentManager()

    def tournament_menu(self):

        while True:
            choice = TournamentView.manage_tournaments_menu()
            match choice:
                case "1":
                    self.create_tournament()
                case "2":
                    self.list_all_tournaments()
                case "b":
                    MainView.main_menu()
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

    def create_tournament(self):
        information = TournamentView().get_tournament_info()
        player = Tournament(**information)
        self.tournament_manager.save_tournament(player)
        MainView.print_success_action(f"Tournament has been added successfully.")
        return True

    def list_all_tournaments(self):
        tournaments = self.tournament_manager.get_all_tournaments()
        TournamentView.display_tournaments(tournaments)
        return True
