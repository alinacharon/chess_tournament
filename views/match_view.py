class MatchView:

    @classmethod
    def manage_matches_menu(cls):
        print(f"\n--- Matches Menu:  ---")
        print("1. Generate matches for the round ---")
        print("2. Manage selected match ---")
        print("b. Back")
        print("q. Quit")
        choice = input("Enter the result of the match: ")
        return choice

    @classmethod
    def display_match(cls, match):
        print(f"\n--- Match: {match.name} ---")
        print(f"  {match.player1.name} vs. {match.player2.name}")

    @classmethod
    def manage_match_menu(cls, match):
        print(f"\n--- Enter Match Result: {match.name} ---")
        print(f"1. {match.player1.name} wins")
        print(f"2. {match.player2.name} wins")
        print("3. Draw")
        choice = input("Enter the result of the match: ")
        return choice

    @classmethod
    def display_matches(cls, matches):
        if not matches:
            print("Please generate matches for this round first.")
        else:
            print("\n--- Available Matches ---\n")
            for i, match in enumerate(matches):
                print(f"{i + 1}. {match.name}: {match}")
