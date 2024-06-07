# app/sources/video/youtube_scrapper.py

from langchain_community.tools import YouTubeSearchTool


class YouTubeSearch:
    def __init__(self):
        self.search_tool = YouTubeSearchTool()

    def search(self, query: str) -> str:
        try:
            return self.search_tool.run(query)
        except Exception as e:
            return f"An error occurred: {e}"

    def get_video(self, query: str) -> str:
        return self.search_tool.get_video(query)
