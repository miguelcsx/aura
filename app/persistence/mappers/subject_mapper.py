# app/persistence/mappers/subject_mapper.py

from app.business.models.subject import Subject
from app.database.models.subject_model import SubjectModel


class SubjectMapper:
    @staticmethod
    def subject_to_model(subject: Subject) -> SubjectModel:
        return SubjectModel(
            id=subject.id,
            name=subject.name,
            description=subject.description,
            user_id=subject.user_id
        )

    @staticmethod
    def model_to_subject(subject_model: SubjectModel) -> Subject:
        return Subject(
            id=subject_model.id,
            name=subject_model.name,
            description=subject_model.description,
            user_id=subject_model.user_id
        )
