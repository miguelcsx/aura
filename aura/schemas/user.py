from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from aura.database.models import Activity, Answer, Question, StudySession


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
        from_attributes = True
        arbitrary_types_allowed = True


class User(UserInDBBase):
    study_sessions: Optional[List[StudySession]] = None
    activities: Optional[List[Activity]] = None
    questions: Optional[List[Question]] = None
    answers: Optional[List[Answer]] = None
