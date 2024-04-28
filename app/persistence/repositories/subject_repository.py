# app/persistence/repositories/subject_repository.py

from app.database.db import SessionLocal
from app.persistence.mappers.subject_mapper import SubjectMapper
from app.database.models.subject_model import SubjectModel


class SubjectRepository:
    def __init__(self):
        self.session = SessionLocal()

    def create(self, subject):
        subject_model = SubjectMapper.subject_to_model(subject)
        self.session.add(subject_model)
        self.session.commit()
        self.session.refresh(subject_model)
        return SubjectMapper.model_to_subject(subject_model)

    def get_by_id(self, id):
        subject_model = self.session.query(
            SubjectModel).filter(SubjectModel.id == id).first()
        return SubjectMapper.model_to_subject(
            subject_model) if subject_model else None

    def get_by_user_id(self, user_id):
        subject_models = self.session.query(SubjectModel).filter(
            SubjectModel.user_id == user_id).all()
        return [SubjectMapper.model_to_subject(
            subject_model) for subject_model in subject_models] if subject_models else None

    def get_all(self):
        subject_models = self.session.query(SubjectModel).all()
        return [SubjectMapper.model_to_subject(
            subject_model) for subject_model in subject_models]

    def update(self, subject):
        subject_model = SubjectMapper.subject_to_model(subject)
        self.session.merge(subject_model)
        self.session.commit()
        self.session.refresh(subject_model)
        return SubjectMapper.model_to_subject(subject_model)

    def delete(self, subject):
        subject_model = SubjectMapper.subject_to_model(subject)
        self.session.delete(subject_model)
        self.session.commit()
        return SubjectMapper.model_to_subject(subject_model)

    def delete_by_user_id(self, user_id):
        subject_models = self.session.query(SubjectModel).filter(
            SubjectModel.user_id == user_id).all()
        for subject_model in subject_models:
            self.session.delete(subject_model)
        self.session.commit()
        return [SubjectMapper.model_to_subject(
            subject_model) for subject_model in subject_models] if subject_models else None
