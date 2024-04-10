# app/server/commands/discord_commands.py

import discord
from app.wikipedia_api.scraper import WikiDocs
from wikipedia.exceptions import PageError
from app.business.services.user_service import UserService
from app.business.services.subject_service import SubjectService
class LogicCommands():

    def __init__(self):
        self.user_service = UserService()
        self.subject_service = SubjectService()

        # Help and brief for the wikipedia command
        self.wikipedia_brief = "Consult a topic on wikipedia"
        self.wikipedia_help = "This command allows you to query a topic directly from wikipedia. You can use it as follows: !wikipedia <theme>"
        
        # Help and brief for the create_subject command
        self.create_subject_brief = "Create a subject"
        self.create_subject_help = "This command allows you to create a subject. You can use it as follows: !create_subject <name> <description>"

    # Function to query a topic from wikipedia
    def wikipedia(self, theme: str) -> discord.Embed | None:
        wiki = WikiDocs(theme)
        
        if wiki.name is None:
            return None
        else:
            embed = discord.Embed(title=wiki.name, description=wiki.content + '\n\n' + wiki.url)
            return embed
            
    # Function to create a subject
    def create_subject(self, name: str, description: str, discord_id: int):
        user_id = self.user_service.get_user_by_discord_id(discord_id).id
        return self.subject_service.create_subject(name, description, user_id)
    