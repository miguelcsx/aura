# app/schemas/user.py

from typing import (
    List,
    Optional,
)
from datetime import datetime
from pydantic import BaseModel
from app.database.models import Activity, Answer, Question, StudySession


class UserBase(BaseModel):
    username: str
    email: str
    role: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class User(UserInDBBase):
    study_sessions: Optional[List["StudySession"]] = []
    activities: Optional[List["Activity"]] = []
    questions: Optional[List["Question"]] = []
    answers: Optional[List["Answer"]] = []
