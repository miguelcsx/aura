# src/app/controllers/user-controller.py

from sqlalchemy.exc import IntegrityError
from app.database.base import Session
from app.models.user import User
from datetime import datetime

class UserController:
    def create_user(self, username, email, password):
        session = Session()
        try:
            user = User(username=username, email=email, password=password)
            session.add(user)
            session.commit()
            print(f"User {username} created successfully")
        except IntegrityError as e:
            print(f"Error: {e.orig}")
            session.rollback()
        finally:
            session.close()

    def read_users(self):
        session = Session()
        users = session.query(User).all()
        session.close()
        return users
    
    def update_user(self, user_id, username=None, email=None, password=None):
        session = Session()
        user = session.query(User).get(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            try:
                session.commit()
                print(f"User {user_id} updated successfully")
            except IntegrityError as e:
                print(f"Error: {e.orig}")
                session.rollback()
        else:
            print(f"User {user_id} not found")
        session.close()

    def delete_user(self, user_id):
        session = Session()
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"User {user_id} deleted successfully")
        else:
            print(f"User {user_id} not found")
        session.close()