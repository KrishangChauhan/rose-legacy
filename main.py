import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🌹 Rose Legacy online as {bot.user}")

extensions = [
    "cogs.legacy",
    "cogs.pvp",
    "cogs.moderation",
    "cogs.economy",
    "cogs.events",
    "cogs.admin"
]

async def load_extensions():
    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print("Loaded", ext)
        except Exception as e:
            print("Failed to load", ext, e)

@bot.event
async def setup_hook():
    await load_extensions()

keep_alive()
bot.run(os.environ["DISCORD_TOKEN"])
