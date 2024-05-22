# app/server/commands/command_tree.py

import discord


def _wikipedia_commands(bot):
    wiki = discord.app_commands.Group(
        name="wikipedia",
        description=bot.wikipedia_command.get_help()["brief"]
    )

    @wiki.command(name="search")
    async def wikipedia_search(
        interaction: discord.Interaction, theme: str
    ) -> None:
        sub_command = "search"
        await interaction.response.send_message(embed=discord.Embed(title=f"Searching {theme} in Wikipedia"))
        consult = bot.wikipedia_command.execute(sub_command, theme)
        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)

    @wiki.command(name="summary")
    async def wikipedia_summary(
        interaction: discord.Interaction, theme: str
    ) -> None:
        sub_command = "summary"
        await interaction.response.send_message(embed=discord.Embed(title=f"Searching {theme} in Wikipedia"))
        consult = bot.wikipedia_command.execute(sub_command, theme)
        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)

    bot.tree.add_command(wiki)


def _create_commands(bot):
    create = discord.app_commands.Group(
        name="create",
        description=bot.create_command.get_help()["brief"]
    )

    @create.command(name="subject")
    async def create_subject(
        interaction: discord.Interaction, name: str, description: str
    ) -> None:
        discord_id = interaction.user.id
        consult = bot.create_command.execute(
            "subject", name, description, discord_id)

        await interaction.response.send_message(consult)

    bot.tree.add_command(create)


def _ai_commands(bot):
    ai = discord.app_commands.Group(
        name="ai",
        description=bot.ai_command.get_help()["brief"]
    )

    @ai.command(name="chat")
    async def ai_chat(
        interaction: discord.Interaction, prompt: str
    ) -> None:
        sub_command = "chat"
        await interaction.response.send_message(embed=discord.Embed(title="Generating text from the AI"))
        consult = bot.ai_command.execute(sub_command, prompt)
        if isinstance(consult, discord.Embed):
            await interaction.edit_original_response(embed=consult)
        else:
            await interaction.response.send_message(consult)

    bot.tree.add_command(ai)


def _study_commands(bot):
    study = discord.app_commands.Group(
        name="study",
        description="Start a study session"
    )

    @study.command(name="session")
    async def start_session(
        interaction: discord.Interaction, duration: float
    ) -> None:
        await bot.study_session_manager.start_session(interaction, duration)

    @study.command(name="time")
    async def remaining_time(
        interaction: discord.Interaction
    ) -> None:
        await bot.study_session_manager.get_remaining_time(interaction)

    bot.tree.add_command(study)


def custom_commands(bot):
    _wikipedia_commands(bot)
    _create_commands(bot)
    _ai_commands(bot)
    _study_commands(bot)
