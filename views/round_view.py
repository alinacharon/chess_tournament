class RoundView:

    @classmethod
    def get_round_selection(cls, rounds):
        if not rounds:
            print("No rounds generated yet. Please generate rounds first.")
            return None
        else:
            print("\n--- Tournament Rounds ---\n")
            for i, round in enumerate(rounds):
                print(f"{i + 1}. {round['name']}")

            while True:
                try:
                    round_index = int(
                        input("Enter the number corresponding to the round to manage (or 0 to go back): "))
                    if 0 <= round_index <= len(rounds):
                        return round_index
                    else:
                        print("Invalid input. Please enter a valid round number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    @classmethod
    def manage_selected_round(cls, round):
        print(f"\n--- Manage {round.name} ---\n")
        print("1. Start the Round")
        print("2. Generate Matches")
        print("3. Select Match")
        print("4. End the Round")
        print("b. Back to selected Tournament")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
