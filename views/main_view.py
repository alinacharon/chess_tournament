class MainView:
    @staticmethod
    def print_success_action(info):
        print(f"\n\x1b[32m{info}\x1b[0m")

    @staticmethod
    def print_error_action():
        print(f"\n\x1b[33mInvalid input. Please enter a valid choice or a valid name.\x1b[0m")

    @staticmethod
    def print_exit():
        print(f"\n\x1b[34mExiting program. Goodbye!\x1b[0m")

    @staticmethod
    def print_info(info):
        print(info)

    @classmethod
    def main_menu(cls):
        print("\n--- Chess Tournament Management ---\n")
        print("1. Manage Players")
        print("2. Manage Tournaments")
        print("3. Generate Reports")
        print("q. Quit")
        choice = input("Enter your choice: ")
        return choice
