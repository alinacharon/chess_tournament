from models.entities.player import Player
from models.managers.player_manager import PlayerManager
from views.player_view import PlayerView


class PlayerController:

    def __init__(self):
        # self.players_view = PlayerView()
        self.player_manager = PlayerManager()

    def player_menu(self):
        return_bool = True
        while return_bool:
            choice = PlayerView.manage_players_menu()
            if choice == '1':
                return_bool = self.create_player()
            if choice == 2:
                return_bool = False
        exit()

    def create_player(self):
        informations = PlayerView().get_players_info()
        player = Player(**informations)
        self.player_manager.save_player(player)
        print(f"Player {player.name} has been added.")
        return True
