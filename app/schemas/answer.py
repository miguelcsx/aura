# app/schemas/answer.py

from typing import (
    Optional,
    List,
)
from pydantic import BaseModel


class AnswerBase(BaseModel):
    answer: str


class AnswerCreate(AnswerBase):
    pass


class AnswerUpdate(AnswerBase):
    pass


class AnswerInDBBase(AnswerBase):
    id: int
    user_id: int
    question_id: int

    class Config:
        orm_mode = True


class Answer(AnswerInDBBase):
    parent_answer: Optional["Answer"] = None
    child_answers: Optional[List["Answer"]] = []


class AnswerInDB(AnswerInDBBase):
    pass
