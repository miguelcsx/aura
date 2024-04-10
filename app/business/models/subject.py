# app/business/models/subject.py

class Subject:
    def __init__(self, id: int = None, name: str = None, description: str = None, user_id: int = None):
        self.id = id
        self.name = name
        self.description = description
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f"Subject(id={self.id}, name={self.name}, description={self.description}, user_id={self.user_id})"