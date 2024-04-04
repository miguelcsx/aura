# src/app/database/db.py

import os
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, sessionmaker

# Specify the path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../../data/db/aura.db")

# Create a SQLite engine
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={'check_same_thread': False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()

# Create the tables in the database
def create_tables() -> None:
    # Check if the tables need to be created
    inspector = inspect(engine)
    if not inspector.get_table_names():
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
