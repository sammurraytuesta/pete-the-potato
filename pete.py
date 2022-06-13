# bot.py
import random

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

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
