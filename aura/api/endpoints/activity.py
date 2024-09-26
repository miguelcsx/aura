# aura/api/endpoints/activity.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from aura.database.session import get_db
from aura.schemas.activity import (
    ActivityCreate,
    ActivityUpdate,
    ActivityInDBBase,
)
from aura.repositories.activity_repository import (
    create_activity,
    get_activity,
    get_activities,
    update_activity,
    delete_activity,
)

router = APIRouter()


@router.post("/activity/", response_model=ActivityInDBBase)
def create_activity_endpoint(
    activity: ActivityCreate, db: Session = Depends(get_db)
) -> ActivityInDBBase:
    return create_activity(db, activity)


@router.get("/activity/{activity_id}", response_model=ActivityInDBBase)
def read_activity(activity_id: int, db: Session = Depends(get_db)) -> ActivityInDBBase:
    activity = get_activity(db, activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity


@router.get("/activity/", response_model=list[ActivityInDBBase])
def read_activities(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
) -> list[ActivityInDBBase]:
    return get_activities(db, skip, limit)


@router.put("/activity/{activity_id}", response_model=ActivityInDBBase)
def update_activity_endpoint(
    activity_id: int, activity: ActivityUpdate, db: Session = Depends(get_db)
) -> ActivityInDBBase:
    db_activity = get_activity(db, activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return update_activity(db, activity_id, activity.model_dump())


@router.delete("/activity/{activity_id}", response_model=ActivityInDBBase)
def delete_activity_endpoint(
    activity_id: int, db: Session = Depends(get_db)
) -> ActivityInDBBase:
    activity = delete_activity(db, activity_id)
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity
