from controllers.player_controller import PlayerController
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.player_controller = PlayerController()

    def main_menu(self):
        return_bool = True
        while return_bool:
            choice = MainView.main_menu()
            if choice == "1":
                return_bool = self.player_controller.player_menu()
            elif choice == "2":
                return_bool = self.tournament_controller.tournament_menu()
            elif choice == "3":
                return_bool = self.report_controller.report_menu()
            elif choice.lower() == "q":
                exit()
