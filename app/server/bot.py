# src/app/discord/bot.py

import discord
from discord.ext import commands
from app.business.services.user_service import UserService
from app.business.services.topic_service import TopicService
from app.server.commands.command_tree import custom_commands
from app.server.commands.wikipedia_command import WikipediaCommand
from app.server.commands.management_command import CreateCommand
from app.server.commands.ai_command import AICommand
from app.server.events.study_session import StudySessionManager
from app.server.commands.video_command import VideoCommand

class Chatbot(commands.Bot):
    def __init__(self, command_prefix: str,
                 intents: discord.Intents, discord_token: str):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.discord_token = discord_token
        self.user_service = UserService()
        self.topic_service = TopicService()

        # Create commands objects
        self.wikipedia_command = WikipediaCommand()
        self.create_command = CreateCommand()
        self.ai_command = AICommand()
        self.video_command = VideoCommand()

        # Create study session manager
        self.study_session_manager = StudySessionManager()

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
        self.topic_service.delete_element_by_object_id(user.id)
        self.subject_service.delete_subjects_by_user_id(user.id)
        self.user_service.delete_user(user.id)
        print(f"{member.name} has left the server")

    async def on_interaction(self, interaction):
        await self.study_session_manager.track_command(interaction)


def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = Chatbot(
        command_prefix="!",
        intents=intents,
        discord_token=discord_token)

    custom_commands(bot)
    return bot
