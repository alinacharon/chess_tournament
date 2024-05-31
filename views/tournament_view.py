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