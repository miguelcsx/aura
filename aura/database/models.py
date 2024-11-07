# aura/database/models.py

from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum as SQLEnum,
    Text,
    DateTime,
)
from sqlalchemy.orm import relationship
from aura.database.session import Base


class UserRole(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class ActivityType(str, Enum):
    question = "question"
    answer = "answer"
    note = "note"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(SQLEnum(UserRole), nullable=False)
    discord_id = Column(
        String, unique=True, nullable=True
    )  # nullable should be False, but it's beta
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    study_sessions = relationship("StudySession", back_populates="user")
    activities = relationship("Activity", back_populates="user")
    questions = relationship("Question", back_populates="user")
    answers = relationship("Answer", back_populates="user")


class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    user = relationship("User", back_populates="study_sessions")
    activities = relationship("Activity", back_populates="study_session")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"))
    type = Column(SQLEnum(ActivityType), nullable=False)
    activity = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="activities")
    study_session = relationship("StudySession", back_populates="activities")

    question = relationship("Question", back_populates="activity", uselist=False)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    question = Column(String)

    user = relationship("User", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
    activity = relationship("Activity", back_populates="question")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer = Column(Text, nullable=False)
    parent_answer_id = Column(Integer, ForeignKey("answers.id"))

    user = relationship("User", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    parent_answer = relationship("Answer", remote_side=[id], backref="child_answers")
