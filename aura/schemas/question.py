# aura/schemas/question.py

from typing import Optional, List
from pydantic import ConfigDict, BaseModel
from aura.database.models import Answer


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
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class Question(QuestionInDBBase):
    answers: Optional[List[Answer]] = None


class QuestionInDB(QuestionInDBBase):
    pass
