"""app/business/services/user_service.py
Module docstring ..."""

from app.business.models.user import User
from app.persistence.repositories.user_repository import UserRepository


class UserService:
    """Class docstring"""

    def __init__(self):
        self.user_repository: UserRepository = UserRepository()

    def create_user(self, discord_id, username):
        user = User(discord_id=discord_id, username=username)
        return self.user_repository.create(user)

    def get_user_by_id(self, id_):
        return self.user_repository.get_by_id(id_)

    def get_user_by_discord_id(self, discord_id):
        return self.user_repository.get_by_element_id(discord_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    def update_user(self, discord_id, username):
        user = User(discord_id=discord_id, username=username)
        return self.user_repository.update(user)

    def delete_user(self, id_):
        user = self.user_repository.get_by_id(id_)
        return self.user_repository.delete(user)

    def delete_user_by_discord_id(self, discord_id):
        # user = self.user_repository.get_by_discord_id(discord_id)
        return self.user_repository.delete_by_element_id(discord_id)
