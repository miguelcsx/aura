from typing import (
    Optional,
    List,
)
from pydantic import BaseModel
from app.database.models import Answer


class QuestionBase(BaseModel):
    question: str


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionInDBBase(QuestionBase):
    id: int
    user_id: int
    activity_id: int

    class Config:
        orm_mode = True


class Question(QuestionInDBBase):
    answers: Optional[List["Answer"]] = []


class QuestionInDB(QuestionInDBBase):
    pass
