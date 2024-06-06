from models.entities.match import Match
from models.entities.round import Round
from models.entities.tournament import Tournament
from models.managers.player_manager import PlayerManager
from models.managers.round_manager import RoundManager
from models.managers.tournament_manager import TournamentManager
from views.main_view import MainView
from views.match_view import MatchView
from views.player_view import PlayerView
from views.round_view import RoundView
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournament_manager = TournamentManager()
        self.player_manager = PlayerManager()
        self.round_manager = RoundManager()

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
        self.handle_tournament_selection(tournament_name)

    def handle_tournament_selection(self, tournament_name):
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
                            if selected_tournament.rounds_num > 0:
                                MainView.print_info(
                                    f"Rounds for the tournament {selected_tournament.name} "
                                    f"have already been generated.")
                            else:
                                self.create_rounds(tournament_name)
                                MainView.print_success_action(
                                    f"Rounds for the tournament {selected_tournament.name} "
                                    f"generated successfully.")
                    case "4":
                        if not selected_tournament.rounds:
                            MainView.print_info("No tournaments yet. Please generate first.")
                        else:
                            self.get_round_selection(tournament_name)
                    case "5":
                        self.add_notes_to_tournament(tournament_name)
                    case "b":
                        TournamentView.manage_tournaments_menu()
                        break
                    case "q":
                        MainView.print_exit()
                        exit()
                    case _:
                        MainView.print_error_action()
                        continue

    def create_tournament(self):
        information = TournamentView().get_tournament_info()

        if self.is_tournament_name_exist(information["name"]):
            MainView.print_info(f"Tournament name '{information['name']}' already exists. Please choose another name.")
            return

        tournament = Tournament(**information)
        self.tournament_manager.tournaments.append(tournament)
        self.tournament_manager.write_in_db(tournament)
        MainView.print_success_action(f"Tournament has been added successfully.")
        return tournament

    def is_tournament_name_exist(self, name):
        for tournament in self.tournament_manager.load_tournaments_from_json():
            if tournament.name == name:
                return True
        return False

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
                round = Round(f"Round {round_num}")
                tournament.rounds.append(round)
                self.tournament_manager.write_in_db(tournament)

    def add_notes_to_tournament(self, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)

        if tournament:
            notes = TournamentView.get_tournament_notes()
            tournament.notes += notes + f" "
            self.tournament_manager.write_in_db(tournament)
            MainView.print_info(f"Notes added to the tournament.")
        else:
            MainView.print_info(f"Tournament {tournament_name} not found")

    def get_round_selection(self, tournament_name):

        rounds_data = self.tournament_manager.get_rounds(tournament_name)

        RoundView.display_rounds(rounds_data)

        while True:
            try:
                round_index = RoundView.get_round_selection()
                if round_index == 0:
                    break
                elif 1 <= round_index <= len(rounds_data):
                    selected_round_data = rounds_data[round_index - 1]
                    selected_round = self.round_manager.round_to_dict(selected_round_data)
                    self.handle_round_choice(selected_round, tournament_name)

                else:
                    MainView.print_error_action()
            except ValueError:
                MainView.print_error_action()

    def handle_round_choice(self, selected_round, tournament_name):
        while True:
            choice = RoundView.manage_selected_round(selected_round)
            match choice:
                case "1":
                    self.generate_matches_for_round(selected_round, tournament_name)
                case "2":
                    if not selected_round.matches:
                        print("Please generate matches for this round first.")
                    else:
                        MatchView.display_matches(selected_round.matches)
                        while True:
                            try:
                                match_index = int(input("Enter the number corresponding to the match to start "
                                                        "(or 0 to go back): "))
                                if match_index == 0:
                                    break
                                elif 1 <= match_index <= len(selected_round.matches):
                                    selected_match = selected_round.matches[match_index - 1]
                                    if selected_match.is_finished():
                                        print(f"{selected_match.name} has already been played.")
                                    else:
                                        pass
                                        # self.start_match(selected_match, tournament)
                                        # break
                                else:
                                    print("Invalid match number. Please try again.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")
                case "b":
                    TournamentView.manage_tournament_menu()
                case "q":
                    print("You have exited the program")
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

    def generate_matches_for_round(self, selected_round, tournament_name):
        if selected_round.matches:
            print(f"Matches for {selected_round.name} have already been generated.")
            return

        tournament = self.tournament_manager.get_tournament(tournament_name)

        if not tournament:
            print(f"Tournament {tournament_name} not found")
            return

        players = sorted(tournament.registered_players, key=lambda p: p.total_points, reverse=True)

        available_players = set(players)
        matches = []

        while len(available_players) >= 2:
            player1 = available_players.pop()
            for player2 in sorted(available_players, key=lambda p: p.total_points, reverse=True):
                if (player1.player_id, player2.player_id) not in tournament.past_matches and \
                        (player2.player_id, player1.player_id) not in tournament.past_matches:
                    available_players.remove(player2)
                    match = Match(f"Match {len(matches) + 1}", selected_round, player1, player2, 0, 0, None)
                    matches.append(match)
                    tournament.past_matches.add((player1.player_id, player2.player_id))
                    selected_round.matches.append(match)
                    self.add_match_to_round(tournament_name, selected_round, match)
                    break

        print(f"\n--- Generated Matches for Round {selected_round.name} ---")
        for match in matches:
            print(f"- {match.name}: {match.player1.name} vs. {match.player2.name}")

    def add_match_to_round(self, tournament_name, selected_round, match):
        round_id = selected_round.round_id
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_info(f"Tournament {tournament_name} not found")
            return

        for round in tournament.rounds:
            if isinstance(round, dict):
                round = self.tournament_manager.get_round(tournament_name, round_id)
            if round.round_id == round_id:
                round.matches.append(match)
                break

        self.tournament_manager.write_in_db(tournament)
