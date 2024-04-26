# src/app/discord/bot.py

import discord
from discord.ext import (
    commands,
    tasks
)
from app.business.services.user_service import UserService
from app.business.services.subject_service import SubjectService
from app.business.services.topic_service import TopicService
from app.server.commands.wikipedia_command import WikipediaCommand
from app.server.commands.management_command import CreateCommand

class Chatbot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, discord_token: str):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.discord_token = discord_token
        self.user_service = UserService()
        self.topic_service = TopicService()
        
        # Create commands objects
        self.wikipedia_command = WikipediaCommand()
        self.create_command = CreateCommand()

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        await self.tree.sync()
    
    async def on_member_join(self, member):
        self.user_service.create_user(member.id, member.name)
        print(f"{member.name} has joined the server")

    async def on_member_update(self, before, after):
        if before.name != after.name:
            self.user_service.update_user(after.id, after.name)
            print(f"{before.name} has changed their name to {after.name}")

    async def on_member_remove(self, member):
        user = self.user_service.get_user_by_discord_id(member.id)
        self.topic_service.delete_topics_by_user_id(user.id)
        self.subject_service.delete_subjects_by_user_id(user.id)
        self.user_service.delete_user(user.id)
        print(f"{member.name} has left the server")

# Function to implement commands to the discord bot
def custom_commands(bot: Chatbot):
    # wikipedia = search summary
    @bot.tree.command(description=bot.wikipedia_command.get_help()["brief"], name="wikipedia")
    async def wikipedia(interaction: discord.Interaction, theme: str, sub_command: str = "search"):
        
        await interaction.response.send_message(embed=discord.Embed(title=f"Serching {theme} in wikipedia"))
        consult = bot.wikipedia_command.execute(sub_command, theme)

        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)




def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = Chatbot(command_prefix="!", intents=intents, discord_token=discord_token)

    custom_commands(bot)
    return bot
