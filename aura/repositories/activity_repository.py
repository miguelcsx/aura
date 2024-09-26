# aura/repositories/activity_repository.py

from sqlalchemy.orm import Session
from aura.database.models import Activity
from aura.schemas.activity import ActivityCreate, ActivityUpdate


def create_activity(db: Session, activity: ActivityCreate) -> Activity:
    db_activity = Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_activity(db: Session, activity_id: int) -> Activity:
    return db.query(Activity).filter(Activity.id == activity_id).first()


def get_activities(db: Session, skip: int = 0, limit: int = 10) -> list[Activity]:
    return db.query(Activity).offset(skip).limit(limit).all()


def update_activity(
    db: Session, activity_id: int, activity: ActivityUpdate
) -> Activity:
    db_activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if db_activity:
        update_data = activity.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_activity, key, value)
        db.commit()
        db.refresh(db_activity)
    return db_activity


def delete_activity(db: Session, activity_id: int) -> Activity:
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if activity:
        db.delete(activity)
        db.commit()
    return activity
