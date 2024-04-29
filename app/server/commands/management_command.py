# app/server/commands/management_commands.py

from app.server.commands.discord_commands import Commands
from app.business.services.user_service import UserService
from app.business.services.subject_service import SubjectService


class CreateCommand(Commands):

    def __init__(self):
        super().__init__()
        self.user_service = UserService()
        self.subject_service = SubjectService()

    def create_subject(self, name: str, description: str, discord_id: str):
        user_id = self.user_service.get_user_by_discord_id(discord_id).id
        return self.subject_service.create_subject(name, description, user_id)

    def execute(self, entity_type: str, name: str,
                description: str, discord_id: str):
        if entity_type == "subject":
            return self.create_subject(name, description, discord_id)
        else:
            return self.get_help(entity_type)

    def get_help(self):
        return {
            "brief": "Create a new entity",
            "help": "This command allows you to create a new entity."
        }
