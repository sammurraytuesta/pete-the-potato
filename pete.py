# bot.py
import os
import random
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="pete", help="responds with a cool fact about potatoes!")
async def pete(ctx):
    file = open("facts.txt", "r")
    potato_facts = []
    for line in file.readlines()[1:]:
        potato_facts.append(line)

    response = random.choice(potato_facts)
    await ctx.send(response)

bot.run(TOKEN)
