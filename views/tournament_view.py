class TournamentView:

    @classmethod
    def manage_tournaments_menu(cls):
        print("\n--- Manage Tournaments ---\n")
        print("1. Create Tournament")
        print("2. List All Tournaments")
        print("3. Select Tournament")
        print("b. Back to Main Menu")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice

    @classmethod
    def get_tournament_info(cls):
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")
        start_date = input("Enter start date (DD/MM/YYYY): ")
        end_date = input("Enter end date (DD/MM/YYYY): ")
        return {"name": name, "location": location, "start_date": start_date, "end_date": end_date}

    @classmethod
    def display_tournaments(cls, tournaments):
        if not tournaments:
            print("No tournaments found.")
        else:
            print("\n--- List of Tournaments ---\n")
            for tournament in tournaments:
                print(tournament)

    @classmethod
    def get_tournament_selection(cls):
        tournament_name = input("Please enter the tournament name: ")
        return tournament_name

    @classmethod
    def manage_selected_tournament(cls, tournament):
        while True:
            print(f"\n--- Manage Tournament: {tournament.name} ---\n")
            print("1. Add Players")
            print("2. View Tournament Details")
            print("3. Generate Rounds")
            print("4. Manage Rounds")
            print("5. Add Notes")
            print("b. Back to Tournaments Menu")
            print("q. Quit")
            choice = input("Enter your choice: ")
            return choice

    @classmethod
    def get_player_selection(cls):
        player_index = int(input("Enter the number corresponding to the player to add (or 0 to finish): "))
        return player_index

    @classmethod
    def get_tournament_notes(cls):
        tournament_notes = input("Enter your tournament notes here: ")
        return tournament_notes

    @classmethod
    def display_rounds(cls, rounds):
        if not rounds:
            print("No rounds generated yet. Please generate rounds first.")
        else:
            print("\n--- Tournament Rounds ---\n")
            for i, round in enumerate(rounds):
                print(f"{i + 1}. {round.name}")

    @classmethod
    def get_round_selection(cls):
        round_index = int(input("Enter the number corresponding to the round to manage (or 0 to go back): "))
        return round_index
