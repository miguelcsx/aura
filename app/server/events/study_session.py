# app/server/events/study_session.py

import os
import csv
from datetime import datetime, timedelta
import discord
from discord.ext import tasks


class StudySessionManager:
    def __init__(self) -> None:
        self.active_sessions = {}

    async def start_session(self, interaction: discord.Interaction, duration: float):
        user_id = interaction.user.id
        if user_id in self.active_sessions:
            await interaction.response.send_message("You already have an active session.")
            return

        end_time = datetime.utcnow() + timedelta(minutes=duration)
        self.active_sessions[user_id] = {
            'start_time': datetime.utcnow(),
            'end_time': end_time,
            'data': [],
        }
        await interaction.response.send_message(f"Study session started.\nDuration: {format_time(duration)}.")
        # Schedule the end session
        self.end_session.start(interaction)

    async def track_command(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        if user_id in self.active_sessions:
            session_data = self.active_sessions[user_id]['data']
            session_data.append({
                'timestamp': datetime.utcnow().isoformat(),
                'command': interaction.data.get('name', ''),
                'options': interaction.data.get('options', [])
            })

    async def get_remaining_time(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        if user_id in self.active_sessions:
            remaining_time = self.active_sessions[user_id]['end_time'] - datetime.utcnow()
            remaining_time = format_time(remaining_time.total_seconds())
            await interaction.response.send_message(f"Remaining time: {remaining_time}")
        else:
            await interaction.response.send_message("You do not have an active session.")

    @tasks.loop(seconds=1)
    async def end_session(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        if user_id in self.active_sessions:
            if datetime.utcnow() >= self.active_sessions[user_id]['end_time']:
                session_data = self.active_sessions.pop(user_id)
                await self.generate_report(interaction, session_data)
                await interaction.followup.send("Study session ended.")
                self.end_session.stop()

    async def generate_report(self, interaction: discord.Interaction, session_data: list):
        user_id = interaction.user.id
        user_folder = os.path.join("data", "reports", str(user_id))
        # Create the user folder if it does not exist
        os.makedirs(user_folder, exist_ok=True)

        filename = f"{user_id}_{datetime.utcnow().isoformat()}_session.csv"
        report_path = os.path.join(user_folder, filename)
        with open(report_path, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['timestamp', 'command', 'options']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for data in session_data['data']:
                writer.writerow(data)

        await interaction.user.send(file=discord.File(report_path))
        await interaction.followup.send("Session report generated.")


def format_time(minutes: float) -> str:
    # Convert floating-point minutes to seconds
    total_seconds = int(minutes * 60)

    # Convert total seconds to a timedelta object
    td = timedelta(seconds=total_seconds)

    # Extract days, hours, minutes, and seconds
    days = td.days
    remaining_seconds = td.seconds
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Build the formatted string
    parts = []
    if days > 0:
        parts.append(f"{days} {'day' if days == 1 else 'days'}")
    if hours > 0:
        parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
    if minutes > 0:
        parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
    if seconds > 0:
        parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    # Join the parts with commas and 'and'
    if len(parts) > 1:
        return ', '.join(parts[:-1]) + f" and {parts[-1]}"
    elif len(parts) == 1:
        return parts[0]
    else:
        return "0 minutes"
