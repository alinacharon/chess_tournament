from controllers.player_controller import PlayerController
from views.main_view import MainView


class MainController:
    def __init__(self):
        # self.main_view = MainView()
        self.player_controller = PlayerController()

    def main_menu(self):
        return_bool = True
        while return_bool:
            choice = MainView.main_menu()
            if choice == '1':
                return_bool = self.player_controller.player_menu()
            if choice == 2:
                return_bool = False
        exit()
