"""app/persistence/mappers/user_mapper.py
Module docstring ..."""

from app.business.models.user import User
from app.database.models.user_model import UserModel
from app.persistence.mappers.mapper import Mapper


class UserMapper(Mapper):
    """Class docstring"""

    @staticmethod
    def element_to_model(element: User) -> UserModel:
        return UserModel(
            id=element.id,
            discord_id=element.discord_id,
            username=element.username,
            created_at=element.created_at,
            subjects=element.subjects,
        )

    @staticmethod
    def element_to_object(element: UserModel) -> User:
        return User(
            id=element.id,
            discord_id=element.discord_id,
            username=element.username,
            created_at=element.created_at,
            subjects=element.subjects,
        )
