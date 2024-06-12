class ReportsView:

    @classmethod
    def generate_reports_menu(cls):
        print("\n--- Generate Reports ---\n")
        print("1. List of all players in alphabetical order")
        print("2. List of all tournaments")
        print("3. Report for a specific tournament (name and dates)")
        print("4. List of tournament players in alphabetical order")
        print("5. List of all rounds and matches in a tournament")
        print("b. Back to Main Menu")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
