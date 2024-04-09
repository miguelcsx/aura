# app/persistence/repositories/user_repository.py

from app.database.db import SessionLocal
from app.persistence.mappers.user_mapper import UserMapper
from app.database.models.user_model import UserModel

class UserRepository:
    def __init__(self):
        self.session = SessionLocal()

    def create(self, user):
        user_model = UserMapper.user_to_model(user)
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return UserMapper.model_to_user(user_model)
    
    def get_by_id(self, id):
        user_model = self.session.query(UserModel).filter(UserModel.id == id).first()
        return UserMapper.model_to_user(user_model) if user_model else None

    def get_by_discord_id(self, discord_id):
        user_model = self.session.query(UserModel).filter(UserModel.discord_id == discord_id).first()
        return UserMapper.model_to_user(user_model) if user_model else None
    
    def get_all(self):
        user_models = self.session.query(UserModel).all()
        return [UserMapper.model_to_user(user_model) for user_model in user_models]
    
    def update(self, user):
        user_model = UserMapper.user_to_model(user)
        self.session.merge(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return UserMapper.model_to_user(user_model)
    
    def delete(self, user):
        user_model = UserMapper.user_to_model(user)
        self.session.delete(user_model)
        self.session.commit()
        return UserMapper.model_to_user(user_model)

    def discord_delete(self, discord_id):
        user_model = self.session.query(UserModel).filter(UserModel.discord_id == discord_id).first()
        self.session.delete(user_model)
        self.session.commit()
        return UserMapper.model_to_user(user_model)
