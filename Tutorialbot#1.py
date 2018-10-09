import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type !gen'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Members')
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content.startswith('!gen'):
        randomlist = ['emiliogiraltnorro@hotmail.com:emilio2003','felix@methe.de:felix1505','mangysage@gmail.com:Scoobi71@','pashodidi@abv.bg:Husjern20','peyjames13@gmail.com:gobears34','philipp.rahrbach@gmx.de:Philipp2003!!...','pratt.trevor@rocketmail.com:s1937tap','enco.juricev555@gmail.com:1234enco','christenson03@gmail.com:Samuel03','perezisaiah843@gmail.com:hectorxd27','s.ribich95@gmail.com:steben01256!','rembrandt132010@gmail.com:66018530','ludvigekelof@gmail.com:kattenbosse1','martinbruraas@gmail.com:Beretta1','hellespont24@hotmail.com:Exia2012','brown_521@msn.com:Monty123','knoll1749@charter.net:Thunder523','xbungalowx@gmail.com:Jailbird2','seanjean1324@gmail.com:killerjet57']
        await client.send_message(message.author,(random.choice(randomlist)))
        await client.send_message(message.channel,('Check Your DM :smiley:'))
        await client.send_message(message.author,'Bot by @Blue Gaming#5147')

 client.run("TOKEN")
