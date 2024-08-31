# app/api/endpoints/courses.py

from fastapi import (
    APIRouter,
    Depends,
#    HTTPException,
)
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.course import (
    CourseCreate,
#    CourseUpdate,
    CourseInDBBase,
)
from app.repositories.course_repository import (
    create_course,
)

router = APIRouter()

@router.post("/courses/", response_model=CourseInDBBase)
def create_course_endpoint(
    course: CourseCreate,
    db: Session = Depends(get_db)
) -> CourseInDBBase:
    return create_course(db, course)
