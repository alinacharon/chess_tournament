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
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_invalid_input()
                    continue

    def create_player(self):
        information = PlayerView().get_players_info()
        player = Player(**information)

        if self.is_player_id_exist(information["player_id"]):
            MainView.print_error_action(f"The player with this ID' {information['player_id']}' "
                                        f"already exists.")

        else:
            self.player_manager.write_in_db(player)
            MainView.print_success_action(f"Player {player.name} has been added.")
            return True

    def is_player_id_exist(self, player_id):
        for player in self.player_manager.load_players_from_json():
            if player.player_id == player_id:
                return True
        return False

    def list_all_players(self):
        players = self.player_manager.get_all_players()
        PlayerView.display_players(players)
        return True
