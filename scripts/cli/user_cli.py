# scripts/cli/user_cli.py

from app.database.db import create_tables
from app.presentation.views.user_view import UserView

def run_user_cli():

    # Create the tables in the database
    create_tables()

    user_view = UserView()

    while True:
        print("\nAura User Management")
        print("1. Create user")
        print("2. Get user by id")
        print("3. Get user by discord id")
        print("4. Get all users")
        print("5. Update user")
        print("6. Delete user")
        print("0. Exit")

        choice = input("Enter choice (0-6): ")

        if choice == "1":
            user_view.create_user()
        elif choice == "2":
            user_view.get_user_by_id()
        elif choice == "3":
            user_view.get_user_by_discord_id()
        elif choice == "4":
            user_view.get_all_users()
        elif choice == "5":
            user_view.update_user()
        elif choice == "6":
            user_view.delete_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_user_cli()
