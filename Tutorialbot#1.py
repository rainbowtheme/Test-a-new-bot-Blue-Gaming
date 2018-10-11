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
async def on_message(message):
    if message.content == !gen
var accounts = ["account1", "account2", "account3"]
var account = 
items[Math.floor(Math.random()*items.length)];
message.author.send("Your alt is: " + account)

client.run(os.getenv("TOKEN"))
