from datetime import datetime

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
            break

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
                                    f"Rounds for the tournament '{selected_tournament.name}' "
                                    f"have already been generated.")
                            else:
                                self.create_rounds(tournament_name)
                                MainView.print_success_action(
                                    f"Rounds for the tournament {selected_tournament.name} "
                                    f"generated successfully.")
                    case "4":
                        if not selected_tournament.rounds:
                            MainView.print_info("\nNo rounds yet. Please generate first.")
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
                    if selected_player in tournament.registered_players:
                        MainView.print_info(f"\n{selected_player.name} is already registered for this tournament.\n")
                        continue
                    else:
                        self.add_player_to_tournament(tournament_name, selected_player)
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
                    self.handle_selected_round(selected_round, tournament_name)

                else:
                    MainView.print_error_action()
            except ValueError:
                MainView.print_error_action()
            break

    def handle_selected_round(self, selected_round, tournament_name):
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
                                match_index = MatchView.get_match_selection()
                                if match_index == 0:
                                    break
                                elif 1 <= match_index <= len(selected_round.matches):
                                    selected_match = selected_round.matches[match_index - 1]
                                    self.handle_match_choice(selected_round, selected_match, tournament_name)

                            except ValueError:
                                MainView.print_error_action()
                case "b":
                    TournamentView.manage_tournaments_menu()
                case "q":
                    MainView.print_exit()
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

    def handle_match_choice(self, selected_round, selected_match, tournament_name):

        while True:
            choice = MatchView.manage_match_selection(selected_match)
            match choice:
                case "1":
                    self.start_match(selected_round, tournament_name)
                case "2":
                    if selected_round.start_date is None:
                        MainView.print_info("The match is not started. Please start the match first.")
                    elif selected_match.score1 == 0 and selected_match.score2 == 0:
                        self.handle_match_result(tournament_name, selected_round, selected_match)
                    else:
                        MainView.print_info(f"The match {selected_match.name} has been already played")
                case "b":
                    TournamentView.manage_tournaments_menu()
                case "q":
                    MainView.print_exit()
                    exit()
                case _:
                    MainView.print_error_action()
                    continue

    def start_match(self, selected_round, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)

        if selected_round.start_date is None:
            selected_round.start_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            for round in tournament.rounds:
                if round.round_id == selected_round.round_id:
                    round.start_date = selected_round.start_date
                    break
            self.tournament_manager.write_in_db(tournament)
            MainView.print_success_action("You have successfully started the match!")
        else:
            MainView.print_info("You have already started the match!")

    def handle_match_result(self, tournament_name, selected_round, selected_match):
        tournament = self.tournament_manager.get_tournament(tournament_name)
        while True:
            choice = MatchView.set_match_result_menu(selected_match)
            match choice:
                case "1":
                    selected_match.set_result(selected_match.player1)
                    selected_match.player1.total_points += 1
                    break
                case "2":
                    selected_match.set_result(selected_match.player2)
                    selected_match.player2.total_points += 1
                    break
                case "3":
                    selected_match.set_result(None)
                    selected_match.player1.total_points += 0.5
                    selected_match.player2.total_points += 0.5
                    MainView.print_success_action("Draw match.")
                    break
                case _:
                    MainView.print_error_action()
                    continue

        self.player_manager.save_player(selected_match.player1)
        self.player_manager.save_player(selected_match.player2)
        self.set_end_round_date(selected_round, tournament_name)
        self.update_tournament_with_match_result(tournament, selected_round, selected_match)
        self.tournament_manager.write_in_db(tournament)
        MainView.print_success_action(f"'{selected_match.name}' ended successfully.")

    def update_tournament_with_match_result(self, tournament, selected_round, selected_match):
        for round in tournament.rounds:
            if round.round_id == selected_round.round_id:
                for match in round.matches:
                    if match.match_id == selected_match.match_id:
                        match.winner = selected_match.winner
                        match.score1 = selected_match.score1
                        match.score2 = selected_match.score2
                        break

    def set_end_round_date(self, selected_round, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)
        print("Checking if all matches are finished...")
        if self.round_is_finished(selected_round, tournament_name):
            selected_round.end_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"All matches finished, setting end date: {selected_round.end_date}")
            for round in tournament.rounds:
                if round.round_id == selected_round.round_id:
                    round.end_date = selected_round.end_date
                    break
            self.tournament_manager.write_in_db(tournament)
            MainView.print_success_action("The current round has been ended!")
        else:
            print("Not all matches are finished yet.")

    def round_is_finished(self, selected_round, tournament_name):
        tournament = self.tournament_manager.get_tournament(tournament_name)
        if not tournament:
            MainView.print_info(f"Tournament {tournament_name} not found")
            return False

        all_matches_finished = all(match.score1 != 0 and match.score2 != 0 for match in selected_round.matches)

        if all_matches_finished:
            MainView.print_success_action(f"All matches in round '{selected_round.name}' are finished.")
        else:
            MainView.print_info(f"Not all matches in round '{selected_round.name}' are finished.")

        return all_matches_finished
