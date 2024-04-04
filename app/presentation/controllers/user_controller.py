# src/app/presentation/controllers/user_controller.py

from app.business.services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self, discord_id, username):
        return self.user_service.create_user(discord_id, username)
    
    def get_user_by_id(self, id):
        return self.user_service.get_user_by_id(id)
    
    def get_user_by_discord_id(self, discord_id):
        return self.user_service.get_user_by_discord_id(discord_id)
    
    def get_all_users(self):
        return self.user_service.get_all_users()
    
    def update_user(self, discord_id, username):
        return self.user_service.update_user(discord_id, username)
    
    def delete_user(self, id):
        return self.user_service.delete_user(id)

    def delete_user_by_discord_id(self, discord_id):
        return self.user_service.delete_user_by_discord_id(discord_id)
