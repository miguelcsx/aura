from sqlalchemy.orm import Session
from app.database.models import Activity
from app.schemas.activity import ActivityCreate, ActivityUpdate


def create_activity(db: Session, activity: ActivityCreate) -> Activity:
    db_activity = Activity(**activity.dict())
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
    db.query(Activity).filter(Activity.id == activity_id).update(activity.dict())
    db.commit()
    return db.query(Activity).filter(Activity.id == activity_id).first()


def delete_activity(db: Session, activity_id: int) -> Activity:
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if activity:
        db.delete(activity)
        db.commit()
    return activity
