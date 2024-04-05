# src/app/database/models/user_model.py

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.database.db import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String(100), unique=True)
    username = Column(String(50))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User(id={self.id}, discord_id={self.discord_id}, username={self.username}, created_at={self.created_at})>"
