import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
client.remove_command('help')
answers = ["apple", "ball", "cat", "dog", "elephant", "frog", "gun"]


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type !gen'))
    print('Bot is ready.')


@client.command()  
async def test(k : int):
    """Chooses between multiple choices."""
    if 0 <= k <= 50:
        await bot.say("This is your random {} pick".format(k))
        embed = discord.Embed(description='\n'.join(random.choices(answers, k=k)))
        await bot.say(embed=embed)
    else:
        await bot.say("Invalid number")

@test.error
def choose_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.say("Please specify how many")

client.run(os.getenv("TOKEN"))
