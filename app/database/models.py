# app/database/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship
from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Column = Column(Integer, primary_key=True, index=True)
    username: Column = Column(String, unique=True, index=True)
    email: Column = Column(String, unique=True, index=True)
    role: Column = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    courses = relationship("Course", back_populates="creator")
    topics = relationship("Topic", back_populates="created_by")
    study_sessions = relationship("StudySession", back_populates="user")


class Course(Base):
    __tablename__ = "courses"

    id: Column = Column(Integer, primary_key=True, index=True)
    title: Column = Column(String, index=True)
    description: Column = Column(Text)
    creator_id: Column = Column(Integer, ForeignKey("users.id"))
    created_at = Column(String)
    updated_at = Column(String)

    creator = relationship("User", back_populates="courses")
    topics = relationship("Topic", back_populates="course")


class Topic(Base):
    __tablename__ = "topics"

    id: Column = Column(Integer, primary_key=True, index=True)
    title: Column = Column(String, index=True)
    description: Column = Column(Text)
    course_id: Column = Column(Integer, ForeignKey("courses.id"), nullable=True)
    creator_id: Column = Column(Integer, ForeignKey("users.id"))
    created_at: Column = Column(String)
    updated_at: Column = Column(String)

    course = relationship("Course", back_populates="topics")
    created_by = relationship("User", back_populates="topics")
    resources = relationship("Resource", back_populates="topic")
    study_sessions = relationship("StudySession", back_populates="topic")


class Resource(Base):
    __tablename__ = "resources"

    id: Column = Column(Integer, primary_key=True, index=True)
    title: Column = Column(String, index=True)
    description: Column = Column(Text)
    type_of: Column = Column(String)
    url: Column = Column(String)
    topic_id: Column = Column(Integer, ForeignKey("topics.id"))
    creator_id: Column = Column(Integer, ForeignKey("users.id"))
    created_at: Column = Column(String)
    updated_at: Column = Column(String)

    topic = relationship("Topic", back_populates="resources")
    creator = relationship("User")


class StudySession(Base):
    __tablename__ = "study_sessions"

    id: Column = Column(Integer, primary_key=True, index=True)
    user_id: Column = Column(Integer, ForeignKey("users.id"))
    topic_id: Column = Column(Integer, ForeignKey("topics.id"))
    start_time: Column = Column(String)
    end_time: Column = Column(String)
    technique: Column = Column(String)

    user = relationship("User", back_populates="study_sessions")
    topic = relationship("Topic", back_populates="study_sessions")
