"""app/persistence/repositories/user_repository.py
Module docstring ..."""

from app.persistence.repositories.repository import Repository
from app.persistence.mappers.user_mapper import UserMapper
from app.database.models.user_model import UserModel


class UserRepository(Repository):
    """Class docstring"""

    def create(self, element):
        user_model = UserMapper.element_to_model(element)
        self._session.add(user_model)
        self._session.commit()
        self._session.refresh(user_model)
        return UserMapper.element_to_object(user_model)

    def get_by_id(self, id_):
        user_model = (self._session.query(UserModel)
                      .filter(UserModel.id == id_)
                      .first())
        return UserMapper.element_to_object(user_model) if user_model else None

    def get_by_element_id(self, element_id):
        user_model = (self._session.query(UserModel)
                      .filter(UserModel.discord_id == element_id)
                      .first())
        return UserMapper.element_to_object(user_model) if user_model else None

    def get_all(self):
        user_models = self._session.query(UserModel).all()
        return ([UserMapper.element_to_object(user_model)
                 for user_model in user_models])

    def update(self, element):
        user_model = UserMapper.element_to_model(element)
        self._session.merge(user_model)
        self._session.commit()
        self._session.refresh(user_model)
        return UserMapper.element_to_object(user_model)

    def delete(self, element):
        user_model = UserMapper.element_to_model(element)
        self._session.delete(user_model)
        self._session.commit()
        return UserMapper.element_to_object(user_model)

    def delete_by_element_id(self, element_id):
        user_model = (self._session.query(UserModel)
                      .filter(UserModel.discord_id == element_id)
                      .first())
        self._session.delete(user_model)
        self._session.commit()
        return UserMapper.element_to_object(user_model)
