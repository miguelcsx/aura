# src/app/database/base.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLite engine
engine = create_engine("sqlite:///aura.db", echo=True)

# Create the session factory
Session = sessionmaker(bind=engine)

# Create the base model class
Base = declarative_base()
