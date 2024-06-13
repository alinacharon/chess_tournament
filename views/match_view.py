class MatchView:

    @classmethod
    def display_match(cls, match):
        print(f"\n--- Match: {match.name} ---")
        print(f"  {match.player1.name} vs. {match.player2.name}")

    @classmethod
    def get_match_selection(cls):
        match_index = int(input("Enter the number corresponding to the match to set "
                                "(or 0 to go back): "))
        return match_index

    @classmethod
    def manage_match_selection(cls, match):
        print(f"\n--- Menu for {match.name}:  ")
        print("1. Set the match result ")
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

    @classmethod
    def display_generated_matches(cls, selected_round):
        print(f"\n--- Generated Matches for {selected_round.name} ---")
        for match in selected_round.matches:
            print(f"- {match.name}: {match.player1.name} vs. {match.player2.name}")
