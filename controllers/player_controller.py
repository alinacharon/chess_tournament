from models.entities.player import Player
from models.managers.player_manager import PlayerManager
from views.player_view import PlayerView
from views.main_view import MainView


class PlayerController:

    def __init__(self):
        self.player_manager = PlayerManager()

    def player_menu(self):
        return_bool = True
        while return_bool:
            choice = PlayerView.manage_players_menu()
            if choice == "1":
                return_bool = self.create_player()
            if choice == "2":
                return_bool = self.list_all_players()
            elif choice.lower() == "b":
                return_bool = MainView.main_menu()
            elif choice.lower() == "q":
                exit()
        exit()

    def create_player(self):
        information = PlayerView().get_players_info()
        player = Player(**information)
        self.player_manager.save_player(player)
        print(f"Player {player.name} has been added.")
        return True

    def list_all_players(self):
        players = self.player_manager.get_all_players()
        PlayerView.display_players(players)
        return True
