# app/server/commands/wikipedia_command.py

import discord
from app.server.commands.discord_commands import Commands
from app.sources.wiki.wiki_scraper import WikiDocs


class WikipediaCommand(Commands):

    def execute(self, sub_command: str, theme: str) -> discord.Embed:
        wiki = WikiDocs(theme)

        if sub_command == "search":
            return self.search(wiki)
        elif sub_command == "summary":
            return self.summary(wiki)
        else:
            return self.get_help()

    def search(self, wiki: WikiDocs) -> discord.Embed:
        search_results = wiki.search()
        return self.create_embed("Search Results", search_results, "")

    def summary(self, wiki: WikiDocs) -> discord.Embed:
        summary_data = wiki.summary()

        if not summary_data:
            return self.create_embed(
                "Error", "The requested Wikipedia page does not exist.", "")

        if isinstance(summary_data, str):
            suggestions = wiki.search()
            return self.create_embed("Did you mean?", suggestions, "")

        if len(summary_data) < 3:
            return self.create_embed(
                "Error", "Unable to retrieve summary data for the requested Wikipedia page.", "")

        theme, content, url = summary_data

        if theme is None:
            return self.create_embed(
                "Error", "The requested Wikipedia page does not exist.", "")

        return self.create_embed(theme, content, url)

    def get_help(self):
        return {
            "brief": "Access Wikipedia information",
            "help": "This command allows you to search or get a summary of a topic from Wikipedia."
        }
