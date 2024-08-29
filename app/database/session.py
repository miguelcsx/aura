# app/database/session.py

import os
from typing import Generator
from sqlalchemy import (
    create_engine,
    Engine,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
DB_PATH: str = os.path.join(BASE_DIR, "../../data/db/aura.db")

engine: Engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False},
)

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
