# app/business/model/topic.py

class Topic:
    def __init__(self, id: int = None,
                 title: str = None,
                 content: str = None,
                 subject_id: int = None,
                 description: str = None,
                 name: str = None) -> None:
        self.id: int | None = id
        self.title: str | None = title
        self.content: str | None = content
        self.subject_id: int | None = subject_id
        self.name: str | None = name
        self.description: str | None = description

    def __repr__(self):
        return (
            f"<Topic("
            f"id={self.id}, "
            f"title={self.title}, "
            f"content={self.content}, "
            f"subject_id={self.subject_id}"
            ")>"
        )
