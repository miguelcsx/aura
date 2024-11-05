# aura/api/endpoints/user.py

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from aura.database.session import get_db
from aura.schemas.discord_user import (
    DiscordUserCreate,
    DiscordUserUpdate,
    DiscordUserInDBBase,
)
from aura.repositories.discord_user_repository import (
    create_discord_user,
    get_discord_user,
    update_discord_user,
    delete_discord_user,
)

router = APIRouter()


@router.post("/discord_user/", response_model=DiscordUserInDBBase)
def create_discord_user_endpoint(
    discord_user: DiscordUserCreate, db: Session = Depends(get_db)
):
    return create_discord_user(db=db, discord_user=discord_user)


@router.get("/discord_user/{discord_user_id}", response_model=DiscordUserInDBBase)
def get_discord_user_endpoint(discord_user_id: int, db: Session = Depends(get_db)):
    db_discord_user = get_discord_user(db=db, discord_user_id=discord_user_id)
    if db_discord_user is None:
        raise HTTPException(status_code=404, detail="DiscordUser not found")
    return db_discord_user


@router.put("/discord_user/{discord_user_id}", response_model=DiscordUserInDBBase)
def update_discord_user_endpoint(
    discord_user_id: int, discord_user: DiscordUserUpdate, db: Session = Depends(get_db)
):
    db_discord_user = update_discord_user(
        db=db, discord_user_id=discord_user_id, discord_user=discord_user
    )
    if db_discord_user is None:
        raise HTTPException(status_code=404, detail="DiscordUser not found")
    return db_discord_user


@router.delete("/discord_user/{discord_user_id}", response_model=DiscordUserInDBBase)
def delete_discord_user_endpoint(discord_user_id: int, db: Session = Depends(get_db)):
    db_discord_user = delete_discord_user(db=db, discord_user_id=discord_user_id)
    if db_discord_user is None:
        raise HTTPException(status_code=404, detail="DiscordUser not found")
    return db_discord_user
