import discord
from app.wikipedia_api.scraper import WikiDocs
from wikipedia.exceptions import PageError

class LogicCommands():

    wikipedia_help = "This command allows you to query a topic directly from wikipedia. You can use it as follows: !wikipedia <theme>"
    wikipedia_brief = "Consult a topic on wikipedia"


    def wikipedia(self, theme: str) -> discord.Embed | None:
        
        wiki = WikiDocs(theme)
        
        if wiki.name is None:
            return None
        else:
            embed = discord.Embed(title=wiki.name, description=wiki.content + '\n\n' + wiki.url)
            return embed
            