# app/business/services/subject_service.py

from app.business.models.subject import Subject
from app.persistence.repositories.subject_repository import SubjectRepository


class SubjectService:
    def __init__(self):
        self.subject_repository = SubjectRepository()

    def create_subject(self, name, description, user_id):
        subject = Subject(name=name, description=description, user_id=user_id)
        return self.subject_repository.create(subject)

    def get_subject_by_id(self, id):
        return self.subject_repository.get_by_id(id)

    def get_subjects_by_user_id(self, user_id):
        return self.subject_repository.get_by_user_id(user_id)

    def get_all_subjects(self):
        return self.subject_repository.get_all()

    def update_subject(self, id, name, description, user_id):
        subject = Subject(
            id=id,
            name=name,
            description=description,
            user_id=user_id)
        return self.subject_repository.update(subject)

    def delete_subject(self, id):
        subject = self.subject_repository.get_by_id(id)
        return self.subject_repository.delete(subject)

    def delete_subject_by_user_id(self, user_id):
        return self.subject_repository.delete_by_user_id(user_id)
