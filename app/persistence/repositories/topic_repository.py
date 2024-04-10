# app/persistence/repositories/topic_repository.py

from app.database.db import SessionLocal
from app.persistence.mappers.topic_mapper import TopicMapper
from app.database.models.topic_model import TopicModel

class TopicRepository:
    def __init__(self):
        self.session = SessionLocal()

    def create(self, topic):
        topic_model = TopicMapper.topic_to_model(topic)
        self.session.add(topic_model)
        self.session.commit()
        self.session.refresh(topic_model)
        return TopicMapper.model_to_topic(topic_model)
    
    def get_by_id(self, id):
        topic_model = self.session.query(TopicModel).filter(TopicModel.id == id).first()
        return TopicMapper.model_to_topic(topic_model) if topic_model else None
    
    def get_by_subject_id(self, subject_id):
        topic_models = self.session.query(TopicModel).filter(TopicModel.subject_id == subject_id).all()
        return [TopicMapper.model_to_topic(topic_model) for topic_model in topic_models] if topic_models else None
    
    def get_all(self):
        topic_models = self.session.query(TopicModel).all()
        return [TopicMapper.model_to_topic(topic_model) for topic_model in topic_models]
    
    def update(self, topic):
        topic_model = TopicMapper.topic_to_model(topic)
        self.session.merge(topic_model)
        self.session.commit()
        self.session.refresh(topic_model)
        return TopicMapper.model_to_topic(topic_model)
    
    def delete(self, topic):
        topic_model = TopicMapper.topic_to_model(topic)
        self.session.delete(topic_model)
        self.session.commit()
        return TopicMapper.model_to_topic(topic_model)
    
    def delete_by_subject_id(self, subject_id):
        topic_models = self.session.query(TopicModel).filter(TopicModel.subject_id == subject_id).all()
        for topic_model in topic_models:
            self.session.delete(topic_model)
        self.session.commit()
        return [TopicMapper.model_to_topic(topic_model) for topic_model in topic_models] if topic_models else None
