# app/persistence/mappers/user_mapper.py

from app.business.models.user import User
from app.database.models.user_model import UserModel

class UserMapper:
    @staticmethod
    def user_to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            discord_id=user.discord_id,
            username=user.username,
            created_at=user.created_at,
            subjects=user.subjects
        )
    
    @staticmethod
    def model_to_user(user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            discord_id=user_model.discord_id,
            username=user_model.username,
            created_at=user_model.created_at,
            subjects=user_model.subjects
        )
