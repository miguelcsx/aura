# scripts/database_setup.py

from app.database.base import Base, engine
from app.models.user import User

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
