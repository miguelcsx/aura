# src/app/discord/bot.py

import discord
from discord.ext import commands
from app.business.services.user_service import UserService
from app.server.commands.discord_commands import LogicCommands

class Chatbot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, discord_token: str):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.discord_token = discord_token
        self.user_service = UserService()
        self.logic_commands = LogicCommands()
        self.custom_commands()

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
    
    async def on_member_join(self, member):
        self.user_service.create_user(member.id, member.name)
        print(f"{member.name} has joined the server")

    async def on_member_update(self, before, after):
        if before.name != after.name:
            self.user_service.update_user(after.id, after.name)
            print(f"{before.name} has changed their name to {after.name}")

    async def on_member_remove(self, member):
        self.user_service.delete_user_by_discord_id(member.id)
        print(f"{member.name} has left the server")

    # Function to implement commands to the discord bot
    def custom_commands(self):
        @self.command(help=self.logic_commands.wikipedia_help, brief=self.logic_commands.wikipedia_brief)
        async def wikipedia(ctx, theme: str = None):
            if theme is None:
                await ctx.send(self.logic_commands.parameter_error)
            else:
                consult = self.logic_commands.wikipedia(theme)
                if consult is None:
                    await ctx.send(f"{theme} not found")
                else:
                    await ctx.send(embed=consult)

        @self.command(help=self.logic_commands.create_subject_help, brief=self.logic_commands.create_subject_brief)
        async def create_subject(ctx, name: str, description: str):
            response = self.logic_commands.create_subject(name, description, ctx.author.id)
            await ctx.send(response)


def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = Chatbot(command_prefix="!", intents=intents, discord_token=discord_token)

    return bot
