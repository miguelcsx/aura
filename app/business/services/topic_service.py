"""app/business/services/topic_service.py
Module docstring ..."""

from app.business.services.service import Service
from app.business.models.topic import Topic
from app.persistence.repositories.topic_repository import TopicRepository


class TopicService(Service):
    """Class docstring"""

    def __init__(self):
        self.topic_repository: TopicRepository = TopicRepository()

    def create(self, name: str, description: str, subject_id: int):
        topic = Topic(name=name,
                      description=description,
                      subject_id=subject_id)
        return self.topic_repository.create(topic)

    def get_element_by_id(self, id_):
        return self.topic_repository.get_by_id(id_)

    def get_elements_by_object_id(self, id_):
        return self.topic_repository.get_by_element_id(id_)

    def get_all_elements(self):
        return self.topic_repository.get_all()

    def update_element(self, id_, name, description, subject_id):
        topic = Topic(id=id_, name=name,
                      description=description,
                      subject_id=subject_id)
        return self.topic_repository.update(topic)

    def delete_element(self, id_):
        topic = self.topic_repository.get_by_id(id_)
        return self.topic_repository.delete(topic)

    def delete_element_by_object_id(self, element_id):
        return self.topic_repository.delete_by_element_id(element_id)
