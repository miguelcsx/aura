# aura/schemas/user.py

from typing import List, Optional
from datetime import datetime
from pydantic import ConfigDict, BaseModel
from aura.database.models import UserRole, Activity, Answer, Question, StudySession


class UserBase(BaseModel):
    username: str
    email: str
    role: UserRole


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class User(UserInDBBase):
    study_sessions: Optional[List[StudySession]] = None
    activities: Optional[List[Activity]] = None
    questions: Optional[List[Question]] = None
    answers: Optional[List[Answer]] = None
