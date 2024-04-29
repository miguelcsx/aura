"""This module ..."""

from abc import ABC, abstractmethod
from app.database.db import SessionLocal


class Repository(ABC):
    """Insert docstring"""

    def __init__(self):
        self._session = SessionLocal()

    @abstractmethod
    def create(self, element):
        """Insert docstring"""

    @abstractmethod
    def get_by_id(self, id_):
        """Insert docstring"""

    @abstractmethod
    def get_by_element_id(self, element_id):
        """Insert docstring"""

    @abstractmethod
    def get_all(self):
        """Insert docstring"""

    @abstractmethod
    def update(self, element):
        """Insert docstring"""

    @abstractmethod
    def delete(self, element):
        """Insert docstring"""

    @abstractmethod
    def delete_by_element_id(self, element_id):
        """Insert docstring"""
