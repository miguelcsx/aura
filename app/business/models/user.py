# app/business/models/user.py

class User:
    def __init__(self, id: int = None, discord_id: str = None, username: str = None, created_at: str = None, subjects: list = []):
        self.id = id
        self.discord_id = discord_id
        self.username = username
        self.created_at = created_at
        self.subjects = subjects

    def __repr__(self) -> str:
        return f"User(id={self.id}, discord_id={self.discord_id}, username={self.username}, created_at={self.created_at})"
