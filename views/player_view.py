class PlayerView:

    @classmethod
    def manage_players_menu(cls):
        print("\n--- Manage Players ---\n")
        print("1. Add Player")
        print("2. List All Players")
        print("b. Back to Main Menu")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice

    @classmethod
    def get_players_info(cls):
        last_name = input("Enter player's last name: ")
        first_name = input("Enter player's first name: ")
        birthdate = input("Enter player's birthdate (DD/MM/YYYY): ")
        player_id = input("Enter player's national chess ID (AA12345): ")
        return {"last_name": last_name, "first_name": first_name, "birthdate": birthdate, "player_id": player_id}

    @classmethod
    def display_players(cls, players):
        if not players:
            print("No players found.")
        else:
            print("\n--- List of Players ---\n")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player}")
