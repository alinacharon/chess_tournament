class RoundView:
    @classmethod
    def display_rounds(cls, rounds):
        if not rounds:
            print("No rounds generated yet. Please generate rounds first.")
        else:
            print("\n--- Tournament Rounds ---\n")
            for i, round in enumerate(rounds):
                print(f"{i + 1}. {round['name']}")

    @classmethod
    def get_round_selection(cls):
        round_index = int(input("Enter the number corresponding to the round to manage (or 0 to go back): "))
        return round_index

    @classmethod
    def manage_selected_round(cls, round):
        print(f"\n--- Manage {round.name} ---\n")
        print("1. Start the round")
        print("2. Generate Matches")
        print("3. Select Match")
        print("4. End the round")
        print("b. Back to Round Selection")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
