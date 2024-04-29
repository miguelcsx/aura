"""app/business/services/subject_service.py
Module docstring ..."""

from app.business.models.subject import Subject
from app.persistence.repositories.subject_repository import SubjectRepository


class SubjectService:
    """Class docstrign"""
    
    def __init__(self) -> None:
        self.subject_repository: SubjectRepository = SubjectRepository()

    def create_subject(self,
                       name: str,
                       description: str,
                       user_id: int) -> Subject:
        subject: Subject = Subject(name=name,
                                   description=description,
                                   user_id=user_id)
        return self.subject_repository.create(subject)

    def get_subject_by_id(self, id_: int) -> Subject | None:
        return self.subject_repository.get_by_id(id_)

    def get_subjects_by_user_id(self, user_id: int) -> list[Subject] | None:
        return self.subject_repository.get_by_element_id(user_id)

    def get_all_subjects(self) -> list[Subject]:
        return self.subject_repository.get_all()

    def update_subject(self, id_: int,
                       name: str,
                       description: str,
                       user_id: int) -> Subject:
        subject: Subject = Subject(id=id_, name=name,
                                   description=description,
                                   user_id=user_id)
        return self.subject_repository.update(subject)

    def delete_subject(self, id_: int) -> Subject:
        subject: Subject | None = self.subject_repository.get_by_id(id_)
        return self.subject_repository.delete(subject)

    def delete_subject_by_user_id(self, user_id: int) -> list[Subject] | None:
        return self.subject_repository.delete_by_element_id(user_id)
