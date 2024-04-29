# src/app/discord/bot.py

import discord
from discord.ext import commands
from app.business.services.user_service import UserService
from app.business.services.topic_service import TopicService
from app.server.commands.wikipedia_command import WikipediaCommand
from app.server.commands.management_command import CreateCommand


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

# Function to implement commands to the discord bot


def custom_commands(bot: Chatbot):

    # subcommand groups
    groups: list[discord.app_commands.Group] = []
    wiki: discord.app_commands.Group = discord.app_commands.Group(
        name="wikipedia", description=bot.wikipedia_command.get_help()["brief"])
    groups.append(wiki)
    create: discord.app_commands.Group = discord.app_commands.Group(
        name="create", description=bot.create_command.get_help()["brief"])
    groups.append(create)

    @wiki.command(name="search")
    async def wikipedia_search(
            interaction: discord.Interaction, theme: str) -> None:
        sub_command: str = "search"

        await interaction.response.send_message(embed=discord.Embed(title=f"Serching {theme} in wikipedia"))
        consult = bot.wikipedia_command.execute(sub_command, theme)

        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)

    @wiki.command(name="summary")
    async def wikipedia_summary(
            interaction: discord.Interaction, theme: str) -> None:
        sub_command: str = "summary"

        await interaction.response.send_message(embed=discord.Embed(title=f"Serching {theme} in wikipedia"))
        consult = bot.wikipedia_command.execute(sub_command, theme)

        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)

    @create.command(name="subject")
    async def create_subject(
            interaction: discord.Interaction, name: str, description: str) -> None:

        discord_id = interaction.user.id
        consult = bot.create_command.execute(
            "subject", name, description, discord_id)

        await interaction.response.send_message(consult)

    # add subcommands
    for i in groups:
        bot.tree.add_command(i)


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
