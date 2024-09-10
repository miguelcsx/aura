from typing import Optional
from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from app.database.models import Question


class ActivityType(str, Enum):
    question = "question"


class ActivityBase(BaseModel):
    type: ActivityType
    activity: str
    created_at: datetime


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(ActivityBase):
    pass


class ActivityInDBBase(ActivityBase):
    id: int
    user_id: int
    study_session_id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class Activity(ActivityInDBBase):
    question: Optional[Question] = None


class ActivityInDB(ActivityInDBBase):
    pass
