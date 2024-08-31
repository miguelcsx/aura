# app/schemas/user.py

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True
