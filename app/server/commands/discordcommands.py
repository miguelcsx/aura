import discord
from discord.ext import commands
from wikipediaAPI.scraper import wikidocs

class logiccommands:

    wikipeida_help: str = "This command allows you to query a specific topic directly from wikipedia. To use the command you must do it this way: !wikipedia <subject>"
    wikipedia_brief: str = "Make a query on wikipedia"

    def wikipedia(self, subject: str) -> discord.Embed:
        wiki = wikidocs(subject)
        if wiki.name is None:
            embed: discord.Embed = discord.Embed(title=subject, description="information not found")
        else:
            embed = discord.Embed(title=subject, description= f"{wiki.summary}\n\n{wiki.link}")
        return embed