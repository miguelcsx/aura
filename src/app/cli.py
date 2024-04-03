# src/app/cli.py
import sys
from controllers.user_controller import UserController
from database.base import create_tables

def main():
    # Call create_tables function before accessing the UserController
    create_tables()
    user_controller = UserController()

    if len(sys.argv) < 2:
        print("Usage: python cli.py <command>")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "create_user":
        if len(args) != 3:
            print("Usage: python cli.py create_user <username> <email> <password>")
            sys.exit(1)
        user_controller.create_user(*args)

    elif command == "read_users":
        users = user_controller.read_users()
        for user in users:
            print(user)

    elif command == "update_user":
        if len(args) != 3:
            print("Usage: python cli.py update_user <user_id> <username> <email> <password>")
            sys.exit(1)
        user_controller.update_user(*args)
    
    elif command == "delete_user":
        if len(args) != 1:
            print("Usage: python cli.py delete_user <user_id>")
            sys.exit(1)
        user_controller.delete_user(*args)


if __name__ == "__main__":
    main()
