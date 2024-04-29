"""app/persistence/repositories/topic_repository.py
Module docstring ..."""

from app.persistence.mappers.topic_mapper import TopicMapper
from app.database.models.topic_model import TopicModel
from app.persistence.repositories.repository import Repository


class TopicRepository(Repository):
    """Class docstring"""

    def create(self, element):
        topic_model = TopicMapper.element_to_model(element)
        self._session.add(topic_model)
        self._session.commit()
        self._session.refresh(topic_model)
        return TopicMapper.element_to_object(topic_model)

    def get_by_id(self, id_):
        topic_model = (self._session.query(TopicModel)
                       .filter(TopicModel.id == id_)
                       .first())
        return (TopicMapper.element_to_object(topic_model)
                if topic_model else None)

    def get_by_element_id(self, element_id):
        topic_models = (self._session.query(TopicModel)
                        .filter(TopicModel.subject_id == element_id)
                        .all())
        return ([TopicMapper.element_to_object(topic_model)
                 for topic_model in topic_models]
                if topic_models
                else None)

    def get_all(self):
        topic_models = self._session.query(TopicModel).all()
        return ([TopicMapper.element_to_object(topic_model)
                 for topic_model in topic_models])

    def update(self, element):
        topic_model = TopicMapper.element_to_model(element)
        self._session.merge(topic_model)
        self._session.commit()
        self._session.refresh(topic_model)
        return TopicMapper.element_to_object(topic_model)

    def delete(self, element):
        topic_model = TopicMapper.element_to_model(element)
        self._session.delete(topic_model)
        self._session.commit()
        return TopicMapper.element_to_object(topic_model)

    def delete_by_element_id(self, element_id):
        topic_models = (self._session.query(TopicModel)
                        .filter(TopicModel.subject_id == element_id)
                        .all())
        for topic_model in topic_models:
            self._session.delete(topic_model)
        self._session.commit()
        return ([TopicMapper.element_to_object(topic_model)
                 for topic_model in topic_models]
                if topic_models
                else None)
