# app/database/models/subject_model.py

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base

class SubjectModel(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Subject(id={self.id}, name={self.name}, description={self.description}, user_id={self.user_id})"
