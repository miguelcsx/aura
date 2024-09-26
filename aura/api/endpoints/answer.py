# aura/api/endpoints/answer.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from aura.database.session import get_db
from aura.schemas.answer import (
    AnswerCreate,
    AnswerUpdate,
    AnswerInDBBase,
)
from aura.repositories.answer_repository import (
    create_answer,
    get_answer,
    get_answers,
    update_answer,
    delete_answer,
)

router = APIRouter()


@router.post("/answers/", response_model=AnswerInDBBase)
def create_answer_endpoint(
    answer: AnswerCreate, db: Session = Depends(get_db)
) -> AnswerInDBBase:
    return create_answer(db, answer)


@router.get("/answers/{answer_id}", response_model=AnswerInDBBase)
def read_answer(answer_id: int, db: Session = Depends(get_db)) -> AnswerInDBBase:
    answer = get_answer(db, answer_id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer


@router.get("/answers/", response_model=list[AnswerInDBBase])
def read_answers(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[AnswerInDBBase]:
    return get_answers(db, skip, limit)


@router.put("/answers/{answer_id}", response_model=AnswerInDBBase)
def update_answer_endpoint(
    answer_id: int, answer: AnswerUpdate, db: Session = Depends(get_db)
) -> AnswerInDBBase:
    db_answer = get_answer(db, answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return update_answer(db, answer_id, answer.model_dump())


@router.delete("/answers/{answer_id}", response_model=AnswerInDBBase)
def delete_answer_endpoint(
    answer_id: int, db: Session = Depends(get_db)
) -> AnswerInDBBase:
    answer = delete_answer(db, answer_id)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer
