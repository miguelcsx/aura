# aura/schemas/discord_user.py

from datetime import datetime
from pydantic import BaseModel


class DiscordUserBase(BaseModel):
    discord_id: str
    user_id: int


class DiscordUserCreate(DiscordUserBase):
    pass


class DiscordUserUpdate(DiscordUserBase):
    pass


class DiscordUserInDBBase(DiscordUserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
