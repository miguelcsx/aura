import discord
from discord.ext import commands
from app.business.services.user_service import UserService
from app.server.commands.discord_commands import LogicCommands

class Chatbot(commands.Bot):   
    def __init__(self, command_prefix: str, intents: discord.Intents, discord_token: str):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.discord_token = discord_token
        self.logic_commands = LogicCommands()
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        await self.tree.sync()

def custom_commands(bot: Chatbot):
    
    @bot.tree.command(name="wikipedia", description=bot.logic_commands.wikipedia_brief)
    async def wikipedia(interaction: discord.Interaction, theme: str):

        if theme is None:
            await interaction.response.send_message(bot.logic_commands.parameter_error)
        else:
            consult = bot.logic_commands.wikipedia(theme)
            
            if consult is None:
                await interaction.response.send_message(f"{theme} is not found")
            else:
                await interaction.response.send_message(embed=consult)

    @bot.tree.command(name="create-subject", description=bot.logic_commands.create_subject_brief)
    async def create_subject(interaction: discord.Interaction, name: str, description: str):

        response = bot.logic_commands.create_subject(name, description, interaction.user.id)
        await interaction.response.send_message(response)


def setup_bot(discrod_token: str) -> None:
    intents = discord.Intents.all()

    bot = Chatbot(command_prefix='!', intents=intents, discord_token=discrod_token)

    custom_commands(bot)
    return bot
