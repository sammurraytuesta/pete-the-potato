# bot.py
import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='pete')
async def pete(ctx):
    potato_facts = [
        "potatoes are cool",
        "potato is spelled p-o-t-a-t-o"
    ]

    response = random.choice(potato_facts)
    await ctx.send(response)

bot.run(TOKEN)
