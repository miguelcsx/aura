# app/business/model/topic.py

class Topic:
    def __init__(self, id: int = None, title: str = None, content: str = None, subject_id: int = None):
        self.id = id
        self.title = title
        self.content = content
        self.subject_id = subject_id

    def __repr__(self):
        return f"<Topic(id={self.id}, title={self.title}, content={self.content}, subject_id={self.subject_id})>"
