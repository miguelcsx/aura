# aura/schemas/activity.py

from typing import Optional
from datetime import datetime
from pydantic import ConfigDict, BaseModel
from aura.database.models import ActivityType, Question


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
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class Activity(ActivityInDBBase):
    question: Optional[Question] = None


class ActivityInDB(ActivityInDBBase):
    pass
