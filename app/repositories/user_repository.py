# app/repositories/user_repository.py

from sqlalchemy.orm import Session
from app.database.models import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: User) -> User:
    db.query(User).filter(User.id == user_id).update(user)
    db.commit()
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
