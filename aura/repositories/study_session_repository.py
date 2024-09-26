# app/repositories/study_repository.py

from sqlalchemy.orm import Session
from aura.database.models import StudySession
from aura.schemas.study_session import StudySessionCreate, StudySessionUpdate


def create_study_session(
    db: Session, study_session: StudySessionCreate
) -> StudySession:
    db_study_session = StudySession(**study_session.model_dump())
    db.add(db_study_session)
    db.commit()
    db.refresh(db_study_session)
    return db_study_session


def get_study_session(db: Session, study_session_id: int) -> StudySession:
    return db.query(StudySession).filter(StudySession.id == study_session_id).first()


def get_study_sessions(
    db: Session, skip: int = 0, limit: int = 10
) -> list[StudySession]:
    return db.query(StudySession).offset(skip).limit(limit).all()


def update_study_session(
    db: Session, study_session_id: int, study_session: StudySessionUpdate
) -> StudySession:
    db.query(StudySession).filter(StudySession.id == study_session_id).update(
        study_session.model_dump()
    )
    db.commit()
    return db.query(StudySession).filter(StudySession.id == study_session_id).first()


def delete_study_session(db: Session, study_session_id: int) -> StudySession:
    study_session = (
        db.query(StudySession).filter(StudySession.id == study_session_id).first()
    )
    if study_session:
        db.delete(study_session)
        db.commit()
    return study_session
