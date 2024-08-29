# app/api/v1/endpoints.py

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session
from app.database.models import (
    User,
    Course,
    Topic,
)
from app.database.session import get_db

router = APIRouter()


@router.get("/users/", response_model=None)
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> list[User]:
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.get("/courses/", response_model=None)
def read_courses(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> list[Course]:
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses


@router.get("/topics/", response_model=None)
def read_topics(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
) -> list[Topic]:
    topics = db.query(Topic).offset(skip).limit(limit).all()
    return topics
