from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from app.database.models import Activity


class StudySessionBase(BaseModel):
    start_time: datetime
    end_time: Optional[datetime] = None


class StudySessionCreate(StudySessionBase):
    pass


class StudySessionUpdate(StudySessionBase):
    pass


class StudySessionInDBBase(StudySessionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class StudySession(StudySessionInDBBase):
    activities: Optional[List[Activity]] = None


class StudySessionInDB(StudySessionInDBBase):
    pass
