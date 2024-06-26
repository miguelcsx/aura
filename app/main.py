# app/main.py

# Load environment variables
import os
from dotenv import load_dotenv
from app.server.bot import setup_bot
from app.database.db import create_tables


def main():
    """docstring"""

    # Check if the tables need to be created
    create_tables()

    # Load the discord token
    load_dotenv()
    discord_token = os.getenv("DISCORD_TOKEN")
    if not discord_token:
        raise ValueError(
            "DISCORD_TOKEN is not set in the environment variables"
            )

    # Load the google api key
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set in the environment variables")

    # Start the bot
    bot = setup_bot(discord_token)
    bot.run(bot.discord_token)


if __name__ == "__main__":
    main()
