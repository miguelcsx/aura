# aura/app/server/commands/ai_command.py

import os
from datetime import datetime
import discord
from app.utils.cmdline import run_npx_command
from app.server.commands.discord_commands import Commands
from app.sources.generative.text_model import TextModel


class AICommand(Commands):

    def execute(self, sub_command: str, *args) -> discord.Embed:
        ai = TextModel()

        if sub_command == "ask":
            return self.ask(ai, *args)
        elif sub_command == "explain":
            return self.explain(ai, *args)
        elif sub_command == "summarize":
            return self.summarize(ai, *args)
        elif sub_command == "mindmap":
            return self.generate_map(ai, *args)
        else:
            return self.get_help()["brief"]

    def ask(self, ai: TextModel, prompt: str) -> discord.Embed:
        response = ai.ask(prompt)
        return self.create_embed(prompt, response, "")

    def explain(self, ai: TextModel, topic: str) -> discord.Embed:
        response = ai.explain(topic)
        return self.create_embed(topic, response, "")

    def summarize(self, ai: TextModel, text: str, type: str = "brief") -> discord.Embed:
        response = ai.summarize(text, type)
        return self.create_embed(text, response, "")

    async def generate_map(self, ai: TextModel, text: str, user_id: str) -> None:
        user_folder = os.path.join("data", "mindmaps", str(user_id))
        # Create the user folder if it does not exist
        os.makedirs(user_folder, exist_ok=True)
        response = ai.create_mindmap(text)
        filename = f"{user_id}_{datetime.utcnow().isoformat()}_mindmap.md"
        mindmap_path = os.path.join(user_folder, filename)
        with open(mindmap_path, "w", encoding="utf-8") as file:
            file.write(response)

        # Create the visual mind map
        run_npx_command("markmap-cli", "--no-open", "--no-toolbar", mindmap_path, "--offline", "-o", f"{mindmap_path}.html")

        os.remove(mindmap_path)

        return f"{mindmap_path}.html"

    def get_help(self):
        return {
            "brief": "Commands to interact with the AI",
            "search": "Generate text from the AI",
            "parameters": ["ask", "prompt"]
        }
