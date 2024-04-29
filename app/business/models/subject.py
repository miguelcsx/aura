# app/business/models/subject.py

class Subject:
    def __init__(self, id: int = None, name: str = None,
                 description: str = None, user_id: int = None,
                 topics: list = None) -> None:
        self.id: int | None = id
        self.name: str | None = name
        self.description: str | None = description
        self.user_id: int | None = user_id
        self.topics: list = topics

    def __repr__(self) -> str:
        return (
            f"Subject("
            f"id={self.id}, "
            f"name={self.name}, "
            f"description={self.description}, "
            f"user_id={self.user_id}"
            ")"
        )
