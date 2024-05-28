class MainView:
    @staticmethod
    def main_menu():
        print("\n--- Chess Tournament Management ---\n")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Reports")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
