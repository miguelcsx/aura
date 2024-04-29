"""app/persistence/mappers/subject_mapper.py
Module docstring ..."""

from app.business.models.subject import Subject
from app.database.models.subject_model import SubjectModel
from app.persistence.mappers.mapper import Mapper


class SubjectMapper(Mapper):
    """Class docstring"""

    @staticmethod
    def element_to_model(element: Subject) -> SubjectModel:
        return SubjectModel(
            id=element.id,
            name=element.name,
            description=element.description,
            user_id=element.user_id,
        )

    @staticmethod
    def element_to_object(element: SubjectModel) -> Subject:
        return Subject(
            id=element.id,
            name=element.name,
            description=element.description,
            user_id=element.user_id,
        )
