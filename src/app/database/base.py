# src/app/database/base.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Specify the custom path
db_path = "../../data/aura.db"

# Create the SQLite engine
engine = create_engine(f"sqlite:///{db_path}", echo=True)

# Create the session factory
Session = sessionmaker(bind=engine)

# Create the base model class
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(engine)
