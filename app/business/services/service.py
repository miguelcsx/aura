"""app/business/services/service.py
Module docstring ..."""

from abc import ABC, abstractmethod


class Service(ABC):
    """Class docstring"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        """Method docstring"""

    @abstractmethod
    def get_element_by_id(self, id_):
        """Method docstring"""

    @abstractmethod
    def get_elements_by_object_id(self, id_):
        """Method docstring"""

    @abstractmethod
    def get_all_elements(self):
        """Method docstring"""

    @abstractmethod
    def update_element(self):
        """Method docstring"""

    @abstractmethod
    def delete_element(self, id_):
        """Method docstring"""

    @abstractmethod
    def delete_element_by_object_id(self, element_id):
        """Method docstring"""
