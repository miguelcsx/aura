# app/persistence/mappers/topic_mapper.py

from app.business.models.topic import Topic
from app.database.models.topic_model import TopicModel


class TopicMapper:
    @staticmethod
    def topic_to_model(topic: Topic) -> TopicModel:
        return TopicModel(
            id=topic.id,
            title=topic.title,
            content=topic.content,
            subject_id=topic.subject_id
        )

    @staticmethod
    def model_to_topic(topic_model: TopicModel) -> Topic:
        return Topic(
            id=topic_model.id,
            title=topic_model.title,
            content=topic_model.content,
            subject_id=topic_model.subject_id
        )
