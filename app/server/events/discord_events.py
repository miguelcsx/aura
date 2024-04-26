# app/server/events/discord_events.py

import discord
from discord.ext import commands
from app.business.services.user_service import UserService
from app.business.services.topic_service import TopicService


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.user_service = UserService()
        self.topic_service = TopicService()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.user_service.create_user(member.id, member.name)
        print(f"{member.name} has joined the server")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.name != after.name:
            self.user_service.update_user(after.id, after.name)
            print(f"{before.name} has changed their name to {after.name}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        user = self.user_service.get_user_by_discord_id(member.id)
        self.topic_service.delete_topics_by_user_id(user.id)
        self.subject_service.delete_subjects_by_user_id(user.id)
        self.user_service.delete_user(user.id)
        print(f"{member.name} has left the server")
