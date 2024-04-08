# src/app/presentation/views/user_view.py

from presentation.controllers.user_controller import UserController

class UserView:
    def __init__(self):
        self.user_controller = UserController()

    def create_user(self):
        discord_id = input("Enter discord id: ")
        username = input("Enter username: ")
        user = self.user_controller.create_user(discord_id, username)
        print(f"User created: {user}")

    def get_user_by_id(self):
        id = int(input("Enter user id: "))
        user = self.user_controller.get_user_by_id(id)
        print(f"User found: {user}")

    def get_user_by_discord_id(self):
        discord_id = input("Enter discord id: ")
        user = self.user_controller.get_user_by_discord_id(discord_id)
        print(f"User found: {user}")

    def get_all_users(self):
        users = self.user_controller.get_all_users()
        print(f"All users: {users}")

    def update_user(self):
        discord_id = input("Enter discord id: ")
        username = input("Enter username: ")
        user = self.user_controller.update_user(discord_id, username)
        print(f"User updated: {user}")

    def delete_user(self):
        id = int(input("Enter user id: "))
        user = self.user_controller.delete_user(id)
        print(f"User deleted: {user}")

    def delete_user_by_discord_id(self):
        discord_id = input("Enter discord id: ")
        user = self.user_controller.delete_user_by_discord_id(discord_id)
        print(f"User deleted: {user}")
