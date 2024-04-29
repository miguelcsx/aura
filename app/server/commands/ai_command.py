# aura/app/server/commands/ai_command.py

from enum import Enum
import discord
from app.server.commands.discord_commands import Commands
from app.sources.llms.google_ai import GoogleAI


class Model(Enum):
    GOOGLE_AI = "google_ai"
    OPEN_AI = "open_ai"


class AICommand(Commands):

    def __init__(self, model: Model = Model.GOOGLE_AI):
        super().__init__()
        self.model = model

    def execute(self, sub_command: str, prompt: str) -> discord.Embed:
        ai = self.get_model()

        if sub_command == "chat":
            return self.chat(ai, prompt)
        else:
            return self.get_help()["brief"]

    def chat(self, ai: GoogleAI, prompt: str) -> discord.Embed:
        response = ai.generate_text(prompt)
        return self.create_embed(prompt, response, "")

    def get_model(self):
        if self.model == Model.GOOGLE_AI:
            return GoogleAI()
        else:
            return None

    def get_help(self):
        return {
            "brief": "Commands to interact with the AI",
            "search": "Generate text from the AI",
            "parameters": ["chat", "prompt"]
        }
