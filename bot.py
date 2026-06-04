import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

EMOJI = "👑"

@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) != EMOJI:
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    channel = guild.get_channel(payload.channel_id)
    if channel is None:
        return

    try:
        message = await channel.fetch_message(payload.message_id)

        if message.thread:
            return

       await message.create_thread(
    name=f"📜 Audiência de {message.author.display_name}",
    auto_archive_duration=1440
        )

    except Exception as e:
        print(f"Erro: {e}")

bot.run(TOKEN)
