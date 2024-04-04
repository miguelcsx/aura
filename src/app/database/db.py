# src/app/database/db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
