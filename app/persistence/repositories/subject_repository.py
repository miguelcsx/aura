"""app/persistence/repositories/subject_repository.py
Module docstring ..."""

from app.persistence.repositories.repository import Repository
from app.persistence.mappers.subject_mapper import SubjectMapper
from app.database.models.subject_model import SubjectModel
from app.business.models.subject import Subject


class SubjectRepository(Repository):
    """Class docstring"""

    def create(self, element: Subject) -> Subject:
        subject_model: SubjectModel = SubjectMapper.element_to_model(object)
        self._session.add(subject_model)
        self._session.commit()
        self._session.refresh(subject_model)
        return SubjectMapper.element_to_object(subject_model)

    def get_by_id(self, id_: int) -> Subject | None:
        subject_model = (self._session.query(SubjectModel)
                         .filter(SubjectModel.id == id_)
                         .first())
        return (SubjectMapper.element_to_object(subject_model)
                if subject_model
                else None)

    def get_by_element_id(self, element_id: int) -> list[Subject] | None:
        subject_models = (self._session.query(SubjectModel)
                          .filter(SubjectModel.user_id == element_id)
                          .all())
        return ([SubjectMapper.element_to_object(subject_model)
                 for subject_model in subject_models]
                if subject_models
                else None)

    def get_all(self) -> list[Subject]:
        subject_models = self._session.query(SubjectModel).all()
        return ([SubjectMapper.element_to_object(subject_model)
                 for subject_model in subject_models])

    def update(self, element: Subject) -> Subject:
        subject_model: SubjectModel = SubjectMapper.element_to_model(element)
        self._session.merge(subject_model)
        self._session.commit()
        self._session.refresh(subject_model)
        return SubjectMapper.element_to_object(subject_model)

    def delete(self, element: Subject) -> Subject:
        subject_model: SubjectModel = SubjectMapper.element_to_model(element)
        self._session.delete(subject_model)
        self._session.commit()
        return SubjectMapper.element_to_object(subject_model)

    def delete_by_element_id(self, element_id: int) -> list[Subject] | None:
        subject_models = (self._session.query(SubjectModel)
                          .filter(SubjectModel.user_id == element_id)
                          .all())
        for subject_model in subject_models:
            self._session.delete(subject_model)
        self._session.commit()
        return ([SubjectMapper.element_to_object(subject_model)
                 for subject_model in subject_models]
                if subject_models
                else None)
