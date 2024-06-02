from models.entities.round import Round
from models.entities.tournament import Tournament
from models.managers.player_manager import PlayerManager
from models.managers.tournament_manager import TournamentManager
from views.main_view import MainView
from views.player_view import PlayerView
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()

    def tournament_menu(self):
        while True:
            choice = TournamentView.manage_tournaments_menu()
            match choice:
                case "1":
                    self.create_tournament()
                case "2":
                    self.list_all_tournaments()
                case "3":
                    self.get_tournament_selection()
                case "b":
                    MainView.main_menu()
                    break
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

    def get_tournament_selection(self):
        tournament_name = TournamentView.get_tournament_selection()
        selected_tournament = self.tournament_manager.get_tournament(tournament_name)
        if not selected_tournament:
            MainView.print_error_action()
        else:
            while True:
                choice = TournamentView.manage_selected_tournament(selected_tournament)
                match choice:
                    case "1":
                        self.add_players_to_tournament(tournament_name)
                    case "2":
                        MainView.print_info(selected_tournament)
                    case "3":
                        if len(selected_tournament.registered_players) < 2:
                            MainView.print_info("Error: Minimum of 2 players required to generate rounds.")
                        else:
                            self.create_rounds(tournament_name)
                            MainView.print_success_action("Rounds generated successfully.")
                    # case "4":
                    #     if not selected_tournament.rounds:
                    #         print("No rounds generated yet. Please generate rounds first.")
                    #     else:
                    #         print("\n--- Tournament Rounds ---\n")
                    #         for i, round in enumerate(selected_tournament.rounds):
                    #             print(f"{i + 1}. {round.name}")
                    #         while True:
                    #             try:
                    #                 round_index = int(input(
                    #                     "Enter the number corresponding to the round to manage (or 0 to go back): "))
                    #                 if round_index == 0:
                    #                     break
                    #                 elif 1 <= round_index <= len(selected_tournament.rounds):
                    #                     selected_round = selected_tournament.rounds[round_index - 1]
                    #                     self.manage_matches_menu(selected_round, selected_tournament)
                    #                     break
                    #                 else:
                    #                     print("Invalid round number. Please try again.")
                    #             except ValueError:
                    #                 print("Invalid input. Please enter a number.")
                    case "5":
                        self.add_notes_to_tournament(tournament_name)
                    case "b":
                        TournamentView.manage_tournaments_menu()
                    case "q":
                        MainView.print_exit()
                        exit()
                    case _:
                        MainView.print_error_action()
                        continue

    def create_tournament(self):
        information = TournamentView().get_tournament_info()
        tournament = Tournament(**information)
        self.tournament_manager.tournaments.append(tournament)
        self.tournament_manager.write_in_db(tournament)
        MainView.print_success_action(f"Tournament has been added successfully.")
        return tournament

    def list_all_tournaments(self):
        tournaments = self.tournament_manager.load_tournaments_from_json()
        TournamentView.display_tournaments(tournaments)
        return True

    def add_players_to_tournament(self, tournament_name):
        players = self.player_manager.get_all_players()
        PlayerView.display_players(players)
        while True:
            try:
                player_index = TournamentView.get_player_selection()
                if player_index == 0:
                    break
                elif 1 <= player_index <= len(players):
                    selected_player = players[player_index - 1]
                    tournament = self.tournament_manager.get_tournament(tournament_name)
                    if not tournament:
                        MainView.print_info(f"Tournament {tournament_name} not found")
                        return
                    if selected_player in tournament.registered_players:
                        MainView.print_info(f"{selected_player.name} is already registered for this tournament.")
                        return
                    else:
                        self.add_player_to_tournament(tournament_name, selected_player)
                else:
                    MainView.print_error_action()
            except ValueError:
                MainView.print_error_action()

    def add_player_to_tournament(self, tournament_name, player):
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if tournament:
            tournament.registered_players.append(player)
            self.tournament_manager.write_in_db(tournament)
            MainView.print_info(f"{player.name} added to the tournament.")
        else:
            MainView.print_info(f"Tournament {tournament_name} not found")

    def create_rounds(self, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)

        if tournament:
            tournament.rounds_num = len(tournament.registered_players) - 1
            for round_num in range(1, tournament.rounds_num + 1):
                round = Round(f"Round {round_num}", self)
                tournament.rounds.append(round)
                self.tournament_manager.write_in_db(tournament)

    # def add_round_to_tournament(self, tournament_name, round):
    #     tournament = self.tournament_manager.get_tournament(tournament_name)
    #     if tournament:
    #         tournament.rounds.append(round)
    #         tournament.rounds_num = len(tournament.rounds)
    #         self.tournament_manager.write_in_db(tournament)
    #
    # def add_past_match(self, match):
    #     self.past_matches.add(match)

    def add_notes_to_tournament(self, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)

        if tournament:
            notes = TournamentView.get_tournament_notes()
            tournament.notes += notes + f" "
            self.tournament_manager.write_in_db(tournament)
            MainView.print_info(f"Notes added to the tournament.")
        else:
            MainView.print_info(f"Tournament {tournament_name} not found")
    #
    # def add_past_match_to_tournament(self, tournament_name, match):
    #     tournament = self.tournament_manager.get_tournament(tournament_name)
    #     if tournament:
    #         Tournament.add_past_match(match)
    #         self.tournament_manager.write_in_db(tournament)
