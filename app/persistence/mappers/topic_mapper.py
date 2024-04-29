"""app/persistence/mappers/topic_mapper.py
Module docstring ..."""

from app.business.models.topic import Topic
from app.database.models.topic_model import TopicModel
from app.persistence.mappers.mapper import Mapper


class TopicMapper(Mapper):
    """Class docstring"""

    @staticmethod
    def element_to_model(element: Topic) -> TopicModel:
        return TopicModel(
            id=element.id,
            title=element.title,
            content=element.content,
            subject_id=element.subject_id,
        )

    @staticmethod
    def element_to_object(element: TopicModel) -> Topic:
        return Topic(
            id=element.id,
            title=element.title,
            content=element.content,
            subject_id=element.subject_id,
        )
