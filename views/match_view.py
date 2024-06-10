class MatchView:

    @classmethod
    def display_match(cls, match):
        print(f"\n--- Match: {match.name} ---")
        print(f"  {match.player1.name} vs. {match.player2.name}")

    @classmethod
    def get_match_selection(cls):
        match_index = int(input("Enter the number corresponding to the match to start "
                                "(or 0 to go back): "))
        return match_index

    @classmethod
    def manage_match_selection(cls, match):
        print(f"\n--- Menu for {match.name}:  ---")
        print("1. Start the match ---")
        print("2. End the match ---")
        print("b. Back")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice

    @classmethod
    def display_matches(cls, matches):
        if not matches:
            print("Please generate matches for this round first.")
        else:
            print("\n--- Available Matches ---\n")
            for i, match in enumerate(matches):
                print(f"{i + 1}. {match.name}: {match}")

    @classmethod
    def set_match_result_menu(cls, match):
        print(f"\n--- Match Result: {match.name} ---")
        print(f"1. {match.player1.name} wins")
        print(f"2. {match.player2.name} wins")
        print("3. Draw")
        choice = input("Enter the result of the match: ")
        return choice

