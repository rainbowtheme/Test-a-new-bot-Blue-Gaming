import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(game=discord.Game(name="Test bot"))

@client.event
async def on_message(message):
    if messga.content.startswith("!ping"):
        msg = "Yes that test Pong!".format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv("TOKEN"))        
