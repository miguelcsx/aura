# src/app/discord/bot.py

import discord
from discord.ext import commands
from business.services.user_service import UserService

class Chatbot(commands.Bot):
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

        self.remove_command('help') #necesario para tener la instancia personalizada del comando    
        @self.command(help="List of available commands")
        async def help(ctx):
            embed = discord.Embed(title="Help", description="List of available commands")
            for command in self.commands:
                embed.add_field(name=command.name, value=command.help, inline=False)
            await ctx.send(embed=embed)
        


def setup_bot(discord_token: str) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = Chatbot(command_prefix="!", intents=intents, discord_token=discord_token)

    return bot
