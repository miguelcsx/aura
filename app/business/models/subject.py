# app/business/models/subject.py

class Subject:
    def __init__(self, id: int = None, name: str = None,
                 description: str = None, user_id: int = None, topics: list = None):
        self.id: int = id
        self.name: str = name
        self.description: str = description
        self.user_id: int = user_id
        self.topics: list = topics

    def __repr__(self) -> str:
        return f"Subject(id={self.id}, name={self.name}, description={self.description}, user_id={self.user_id})"
