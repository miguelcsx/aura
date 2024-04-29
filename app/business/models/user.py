# app/business/models/user.py

class User:
    def __init__(self, id: int = None, discord_id: str = None,
                 username: str = None, created_at: str = None,
                 subjects: list = None) -> None:
        self.id: int | None = id
        self.discord_id: str | None = discord_id
        self.username: str | None = username
        self.created_at: str | None = created_at
        self.subjects: list = subjects

    def __repr__(self) -> str:
        return (
            f"User("
            f"id={self.id}, "
            f"discord_id={self.discord_id}, "
            f"username={self.username}, "
            f"created_at={self.created_at}"
            ")"
        )
