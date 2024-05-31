from controllers.player_controller import PlayerController
from views.main_view import MainView
from controllers.tournament_controller import TournamentController


class MainController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def main_menu(self):
        while True:
            choice = MainView.main_menu()
            match choice:
                case "1":
                    self.player_controller.player_menu()
                case "2":
                    self.tournament_controller.tournament_menu()
                case "3":
                    self.report_controller.report_menu()
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

