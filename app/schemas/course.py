from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class CourseInDBBase(CourseBase):
    id: int

    class Config:
        orm_mode = True
