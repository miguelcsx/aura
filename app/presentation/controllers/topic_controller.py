"""app/presentation/controllers/topic_controller.py
Module docstring ..."""

from app.business.services.topic_service import TopicService


class TopicController:
    def __init__(self):
        self.topic_service = TopicService()

    def create_topic(self, title, content, subject_id):
        return self.topic_service.create_topic(title, content, subject_id)

    def get_topic_by_id(self, id):
        return self.topic_service.get_topic_by_id(id)

    def get_topics_by_subject_id(self, subject_id):
        return self.topic_service.get_topics_by_subject_id(subject_id)

    def get_all_topics(self):
        return self.topic_service.get_all_topics()

    def update_topic(self, id, title, content, subject_id):
        return self.topic_service.update_topic(id, title, content, subject_id)

    def delete_topic(self, id):
        return self.topic_service.delete_topic(id)

    def delete_topics_by_subject_id(self, subject_id):
        return self.topic_service.delete_topics_by_subject_id(subject_id)
