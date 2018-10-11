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
async def ping():
    await client.say('Yes That Ping')

@client.command(pass_context=True)
async def test(ctx):
    await client.say('testing')
    await client.edit_message('tester')
    
client.run(os.getenv("TOKEN"))
