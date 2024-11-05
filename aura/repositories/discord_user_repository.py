# aura/repositories/discord_user_repository.py

from sqlalchemy.orm import Session
from aura.database.models import DiscordUser
from aura.schemas.discord_user import DiscordUserCreate, DiscordUserUpdate


def create_discord_user(db: Session, discord_user: DiscordUserCreate) -> DiscordUser:
    db_discord_user = DiscordUser(**discord_user.model_dump())
    db.add(db_discord_user)
    db.commit()
    db.refresh(db_discord_user)
    return db_discord_user


def get_discord_user(db: Session, discord_user_id: int) -> DiscordUser:
    return db.query(DiscordUser).filter(DiscordUser.id == discord_user_id).first()


def get_discord_users(db: Session, skip: int = 0, limit: int = 10) -> list[DiscordUser]:
    return db.query(DiscordUser).offset(skip).limit(limit).all()


def update_discord_user(
    db: Session, discord_user_id: int, discord_user: DiscordUserUpdate
) -> DiscordUser:
    db_discord_user = (
        db.query(DiscordUser).filter(DiscordUser.id == discord_user_id).first()
    )
    if db_discord_user:
        update_data = discord_user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_discord_user, key, value)
        db.commit()
        db.refresh(db_discord_user)
    return db_discord_user


def delete_discord_user(db: Session, discord_user_id: int) -> DiscordUser:
    discord_user = (
        db.query(DiscordUser).filter(DiscordUser.id == discord_user_id).first()
    )
    if discord_user:
        db.delete(discord_user)
        db.commit()
    return discord_user
