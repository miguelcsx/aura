# src/app/models/user.py

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from database.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

