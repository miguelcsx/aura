# app/server/commands/video_command.py

import discord
from app.server.commands.discord_commands import Commands
from app.sources.video.youtube_scrapper import YouTubeSearch

class VideoCommand(Commands):

    def execute(self, sub_command: str, theme: str) -> discord.Embed:
        youtube = YouTubeSearch()

        if sub_command == "search":
            return self.search(youtube, theme)
        elif sub_command == "video":
            return self.video(youtube, theme)
        else:
            return self.get_help()

    def search(self, youtube: YouTubeSearch, theme: str) -> discord.Embed:
        search_results = youtube.search(theme)
        return self.create_embed("Search Results", search_results, "")

    def video(self, youtube: YouTubeSearch, theme: str) -> discord.Embed:
        video_data = youtube.get_video(theme)

        if not video_data:
            return self.create_embed(
                "Error", "The requested video does not exist.", "")

        return self.create_embed(video_data["title"], video_data["description"], video_data["url"])

    def get_help(self):
        return {
            "brief": "Access YouTube information",
            "help": "This command allows you to search or get a video from YouTube."
        }
