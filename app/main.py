# src/app/main.py

# Load environment variables
import os
from dotenv import load_dotenv
from server.bot import setup_bot
from database.db import create_tables

def main():
    # Check if the tables need to be created
    create_tables()

    # Load the discord token
    load_dotenv()
    discord_token = os.getenv("DISCORD_TOKEN")
    if not discord_token:
        raise ValueError("DISCORD_TOKEN is not set in the environment variables")
    
    # Start the bot
    bot = setup_bot(discord_token)
    bot.run(bot.discord_token)

if __name__ == "__main__":
    main()