# app/database/models.py

from enum import Enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.database.session import Base


class ActivityType(Enum):
    question = "question"


class User(Base):
    __tablename__ = "users"

    id: Column = Column(Integer, primary_key=True, index=True)
    username: Column = Column(String, unique=True, index=True)
    email: Column = Column(String, unique=True, index=True)
    role: Column = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    study_sessions = relationship("StudySession", back_populates="user")
    activities = relationship("Activity", back_populates="user")
    questions = relationship("Question", back_populates="user")
    answers = relationship("Answer", back_populates="user")


class StudySession(Base):
    __tablename__ = "study_sessions"

    id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    start_time: Column = Column(String)
    end_time: Column = Column(String)

    user = relationship("User", back_populates="study_sessions")
    activities = relationship("Activity", back_populates="study_session")


class Activity(Base):
    __tablename__ = "activities"

    id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    study_session_id: Column = Column(Integer, ForeignKey("study_sessions.id"))
    type: Column = Column(Enum(ActivityType), nullable=False)
    activity: Column = Column(String)
    created_at = Column(String)

    user = relationship("User", back_populates="activities")
    study_session = relationship("StudySession", back_populates="activities")

    question = relationship("Question", back_populates="activity", uselist=False)


class Question(Base):
    __tablename__ = "questions"

    id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    activity_id: Column = Column(Integer, ForeignKey("activities.id"))
    question: Column = Column(String)

    user = relationship("User", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
    activity = relationship("Activity", back_populates="question")


class Answer(Base):
    __tablename__ = "answers"

    id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    question_id: Column = Column(Integer, ForeignKey("questions.id"))
    answer: Column = Column(String)

    user = relationship("User", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    parent_answer = relationship(
        "Answer", remote_side=[id], back_populates="child_answers"
    )
    child_answers = relationship(
        "Answer", back_populates="parent_answer", cascade="all, delete-orphan"
    )
