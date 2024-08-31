# app/repositories/course_repository.py

from sqlalchemy.orm import Session
from app.database.models import Course
from app.schemas.course import CourseCreate


def create_course(db: Session, course: CourseCreate) -> Course:
    db_course = Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
