from models.entities.player import Player
from models.managers.player_manager import PlayerManager
from views.main_view import MainView
from views.player_view import PlayerView


class PlayerController:

    def __init__(self):
        self.player_manager = PlayerManager()

    def player_menu(self):

        while True:
            choice = PlayerView.manage_players_menu()
            match choice:
                case "1":
                    self.create_player()
                case "2":
                    self.list_all_players()
                case "b":
                    MainView.main_menu()
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

    def create_player(self):
        information = PlayerView().get_players_info()
        player = Player(**information)
        self.player_manager.write_in_db(player)
        MainView.print_success_action(f"Player {player.name} has been added.")
        return True

    def list_all_players(self):
        players = self.player_manager.get_all_players()
        PlayerView.display_players(players)
        return True
