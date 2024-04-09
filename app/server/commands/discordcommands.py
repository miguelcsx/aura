import discord
from discord.ext import commands
from wikipediaAPI.scraper import wikidocs

class logiccommands:
    def wikipedia(self, subject: str) -> discord.Embed:
        wiki = wikidocs(subject)
        if wiki.name is None:
            embed: discord.Embed = discord.Embed(title=subject, description="information not found")
        else:
            embed = discord.Embed(title=subject, description= f"{wiki.summary}\n\n{wiki.link}")
        return embed