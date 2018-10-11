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

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Members')
    await client.add_roles(member, role)

@bot.command()  
async def choose(k : int):
    """Chooses between multiple choices."""
    if 0 <= k <= 50:
        await bot.say("This is your random {} pick".format(k))
        embed = discord.Embed(description='\n'.join(random.choices(answers, k=k)))
        await bot.say(embed=embed)
    else:
        await bot.say("Invalid number")

client.run(os.getenv("TOKEN"))
