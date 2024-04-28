# app/server/commands/discord_commands.py

from abc import (
    ABC,
    abstractmethod
)
from app.business.services.user_service import UserService
from app.business.services.subject_service import SubjectService


class Commands(ABC):

    parameter_error = "Invalid parameters. Use !help <command> for more information."

    def __init__(self):
        self.user_service = UserService()
        self.subject_service = SubjectService()

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def get_help(self):
        raise NotImplementedError("Subclasses must implement this method")
