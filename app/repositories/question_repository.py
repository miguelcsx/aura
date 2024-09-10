# app/repositories/question_repository.py

from sqlalchemy.orm import Session
from app.database.models import Question
from app.schemas.question import QuestionCreate, QuestionUpdate


def create_question(db: Session, question: QuestionCreate) -> Question:
    db_question = Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question_id: int) -> Question:
    return db.query(Question).filter(Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 10) -> list[Question]:
    return db.query(Question).offset(skip).limit(limit).all()


def update_question(
    db: Session, question_id: int, question: QuestionUpdate
) -> Question:
    db.query(Question).filter(Question.id == question_id).update(question.model_dump())
    db.commit()
    return db.query(Question).filter(Question.id == question_id).first()


def delete_question(db: Session, question_id: int) -> Question:
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
    return question
