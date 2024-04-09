# src/app/discord/bot.py

import discord
from discord.ext import commands
from business.services.user_service import UserService
from server.commands.discordcommands import logiccommands


class Chatbot(commands.Bot, logiccommands):
    def __init__(self, command_prefix: str, intents: discord.Intents, discord_token: str):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.discord_token = discord_token
        self.user_service = UserService()
        self.custom_commands()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.user_service.create_user(member.id, member.name)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.name != after.name:
            self.user_service.update_user(after.id, after.name)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.user_service.delete_user_by_discord_id(member.id)

    def custom_commands(self) -> None:

        @self.command(help=logiccommands.wikipeida_help, brief=logiccommands.wikipedia_brief)
        async def wikipedia(ctx, subject: str=None):   
            await ctx.send(embed=logiccommands().wikipedia(subject))

        


def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = Chatbot(command_prefix="!", intents=intents, discord_token=discord_token)

    return bot
