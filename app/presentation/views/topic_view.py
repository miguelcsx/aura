# app/presentation/views/topic_view.py

from app.presentation.controllers.topic_controller import TopicController
from app.presentation.controllers.subject_controller import SubjectController

class TopicView:
    def __init__(self):
        self.topic_controller = TopicController()
        self.subject_controller = SubjectController()

    def create_topic(self):
        title = input("Enter title: ")
        content = input("Enter content: ")
        subject_id = int(input("Enter subject id: "))
        subject = self.subject_controller.get_subject_by_id(subject_id)
        if subject:
            topic = self.topic_controller.create_topic(title, content, subject.id)
            print(f"Topic created: {topic}")
        else:
            print(f"Subject with id {subject_id} not found")

    def get_topic_by_id(self):
        id = int(input("Enter topic id: "))
        topic = self.topic_controller.get_topic_by_id(id)
        print(f"Topic found: {topic}")

    def get_topics_by_subject_id(self):
        subject_id = int(input("Enter subject id: "))
        topics = self.topic_controller.get_topics_by_subject_id(subject_id)
        print(f"Topics found: {topics}")

    def get_all_topics(self):
        topics = self.topic_controller.get_all_topics()
        print(f"All topics: {topics}")

    def update_topic(self):
        id = int(input("Enter topic id: "))
        topic = self.topic_controller.get_topic_by_id(id)
        
        if topic:
            title = input(f"Enter title (press enter to keep previous: {topic.title}): ")
            content = input(f"Enter content (press enter to keep previous: {topic.content}): ")
            subject_id_input = input(f"Enter subject id (press enter to keep previous: {topic.subject_id}): ")

            # Update title if provided
            if title.strip() != "":
                topic.title = title

            # Update content if provided
            if content.strip() != "":
                topic.content = content

            # Update subject_id if provided
            if subject_id_input.strip() != "":
                subject_id = int(subject_id_input)
                topic.subject_id = subject_id
            else:
                subject_id = topic.subject_id

            subject = self.subject_controller.get_subject_by_id(subject_id)
            if subject:
                topic = self.topic_controller.update_topic(topic.id, topic.title, topic.content, topic.subject_id)
                print(f"Topic updated: {topic}")
            else:
                print(f"Subject with id {subject_id} not found")
        else:
            print(f"Topic with id {id} not found")
    
    def delete_topic(self):
        id = int(input("Enter topic id: "))
        topic = self.topic_controller.get_topic_by_id(id)
        if topic:
            topic = self.topic_controller.delete_topic(id)
            print(f"Topic deleted: {topic}")
        else:
            print(f"Topic with id {id} not found")
    
    def delete_topics_by_subject_id(self):
        subject_id = int(input("Enter subject id: "))
        topics = self.topic_controller.delete_topics_by_subject_id(subject_id)
        print(f"Topics deleted: {topics}")
