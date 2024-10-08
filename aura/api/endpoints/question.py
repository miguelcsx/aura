# aura/api/endpoints/question.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from aura.database.session import get_db
from aura.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
    QuestionInDBBase,
)
from aura.repositories.question_repository import (
    create_question,
    get_question,
    get_questions,
    update_question,
    delete_question,
)

router = APIRouter()


@router.post("/question/", response_model=QuestionInDBBase)
def create_question_endpoint(
    question: QuestionCreate, db: Session = Depends(get_db)
) -> QuestionInDBBase:
    return create_question(db, question)


@router.get("/question/{question_id}", response_model=QuestionInDBBase)
def read_question(question_id: int, db: Session = Depends(get_db)) -> QuestionInDBBase:
    question = get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.get("/question/", response_model=list[QuestionInDBBase])
def read_questions(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[QuestionInDBBase]:
    return get_questions(db, skip, limit)


@router.put("/question/{question_id}", response_model=QuestionInDBBase)
def update_question_endpoint(
    question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)
) -> QuestionInDBBase:
    db_question = get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return update_question(db, question_id, question.model_dump())


@router.delete("/question/{question_id}", response_model=QuestionInDBBase)
def delete_question_endpoint(
    question_id: int, db: Session = Depends(get_db)
) -> QuestionInDBBase:
    question = delete_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question
