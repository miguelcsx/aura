# app/database/models/topic_model.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db import Base

class TopicModel(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey('subjects.id'))

    def __repr__(self):
        return f"<Topic(id={self.id}, title={self.title}, content={self.content}, subject_id={self.subject_id})>"
