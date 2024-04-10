# app/database/models/user_model.py

from __future__ import annotations
from datetime import datetime
from typing import List
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db import Base
from app.database.models.subject_model import SubjectModel

class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    discord_id: Mapped[str] = mapped_column(String, unique = True)
    username: Mapped[str] = mapped_column(String)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    subjects: Mapped[List["SubjectModel"]] = relationship()

    def __repr__(self):
        return f"<User(id={self.id}, discord_id={self.discord_id}, username={self.username}, created_at={self.created_at})>"
