# app/api/endpoints/study_session.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.study_session import (
    StudySessionCreate,
    StudySessionUpdate,
    StudySessionInDBBase,
)
from app.repositories.study_session_repository import (
    create_study_session,
    get_study_session,
    get_study_sessions,
    update_study_session,
    delete_study_session,
)

router = APIRouter()


@router.post("/study_sessions/", response_model=StudySessionInDBBase)
def create_study_session_endpoint(
    study_session: StudySessionCreate, db: Session = Depends(get_db)
) -> StudySessionInDBBase:
    return create_study_session(db, study_session)


@router.get("/study_sessions/{study_session_id}", response_model=StudySessionInDBBase)
def read_study_session(
    study_session_id: int, db: Session = Depends(get_db)
) -> StudySessionInDBBase:
    study_session = get_study_session(db, study_session_id)
    if study_session is None:
        raise HTTPException(status_code=404, detail="StudySession not found")
    return study_session


@router.get("/study_sessions/", response_model=list[StudySessionInDBBase])
def read_study_sessions(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[StudySessionInDBBase]:
    return get_study_sessions(db, skip, limit)


@router.put("/study_sessions/{study_session_id}", response_model=StudySessionInDBBase)
def update_study_session_endpoint(
    study_session_id: int,
    study_session: StudySessionUpdate,
    db: Session = Depends(get_db),
) -> StudySessionInDBBase:
    db_study_session = get_study_session(db, study_session_id)
    if db_study_session is None:
        raise HTTPException(status_code=404, detail="StudySession not found")
    return update_study_session(db, study_session_id, study_session.model_dump())


@router.delete(
    "/study_sessions/{study_session_id}", response_model=StudySessionInDBBase
)
def delete_study_session_endpoint(
    study_session_id: int, db: Session = Depends(get_db)
) -> StudySessionInDBBase:
    study_session = delete_study_session(db, study_session_id)
    if study_session is None:
        raise HTTPException(status_code=404, detail="StudySession not found")
    return study_session
