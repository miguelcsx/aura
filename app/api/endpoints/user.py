# app/api/endpoints/user.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserInDBBase,
)
from app.repositories.user_repository import (
    create_user,
    get_user,
    get_users,
    update_user,
    delete_user,
)

router = APIRouter()


@router.post("/users/", response_model=UserInDBBase)
def create_user_endpoint(
    user: UserCreate, db: Session = Depends(get_db)
) -> UserInDBBase:
    return create_user(db, user)


@router.get("/users/{user_id}", response_model=UserInDBBase)
def read_user(user_id: int, db: Session = Depends(get_db)) -> UserInDBBase:
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=list[UserInDBBase])
def read_users(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[UserInDBBase]:
    return get_users(db, skip, limit)


@router.put("/users/{user_id}", response_model=UserInDBBase)
def update_user_endpoint(
    user_id: int, user: UserUpdate, db: Session = Depends(get_db)
) -> UserInDBBase:
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db, user_id, user.model_dump())


@router.delete("/users/{user_id}", response_model=UserInDBBase)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)) -> UserInDBBase:
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
