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
        self.custom_commands()

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
    
    async def on_member_join(self, member):
        self.user_service.create_user(member.id, member.name)

    async def on_member_update(self, before, after):
        if before.name != after.name:
            self.user_service.update_user(after.id, after.name)

    async def on_member_remove(self, member):
        self.user_service.delete_user_by_discord_id(member.id)

    # Function to implement commands to the discord bot
    def custom_commands(self):
        @self.command(help=LogicCommands.wikipedia_help, brief=LogicCommands.wikipedia_brief)
        async def wikipedia(ctx, theme: str):
            consult = LogicCommands().wikipedia(theme)
            if consult is None:
                await ctx.send(f"{theme} not found")
            else:
                await ctx.send(embed=consult)

        @self.command(help= LogicCommands.wikipedia_help, brief= LogicCommands.wikipedia_brief)
        async def wikipedia(ctx, theme: str):
            consult = LogicCommands().wikipedia(theme)

            if consult is None:
                await ctx.send(f"{theme} not found")
            else:
                await ctx.send(embed=consult)

def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = Chatbot(command_prefix="!", intents=intents, discord_token=discord_token)

    return bot
