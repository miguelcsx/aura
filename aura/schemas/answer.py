# aura/schemas/answer.py

from typing import Optional, List
from pydantic import ConfigDict, BaseModel
from aura.database.models import Answer


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
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


# pylint: disable=function-redefined
class Answer(AnswerInDBBase):
    parent_answer: Optional[Answer] = None
    child_answers: Optional[List[Answer]] = None


class AnswerInDB(AnswerInDBBase):
    pass
