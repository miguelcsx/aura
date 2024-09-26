from sqlalchemy.orm import Session
from aura.database.models import Answer
from aura.schemas.answer import AnswerCreate, AnswerUpdate


def create_answer(db: Session, answer: AnswerCreate) -> Answer:
    db_answer = Answer(**answer.dict())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_answer(db: Session, answer_id: int) -> Answer:
    return db.query(Answer).filter(Answer.id == answer_id).first()


def get_answers(db: Session, skip: int = 0, limit: int = 10) -> list[Answer]:
    return db.query(Answer).offset(skip).limit(limit).all()


def update_answer(db: Session, answer_id: int, answer: AnswerUpdate) -> Answer:
    db.query(Answer).filter(Answer.id == answer_id).update(answer.dict())
    db.commit()
    return db.query(Answer).filter(Answer.id == answer_id).first()


def delete_answer(db: Session, answer_id: int) -> Answer:
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        db.delete(answer)
        db.commit()
    return answer
