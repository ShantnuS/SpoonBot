######################
#### SpoonBot 0.1 ####
######################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

Bot = commands.Bot(command_prefix='', case_insensitive=True)
count = 0

@Bot.event
async def on_ready():
    print("I'm ready! My name: " + Bot.user.name + " and my ID: " + Bot.user.id)

def sayShutUp():
    return "Shut Up"

def sayYes():
    global count
    count += 1
    if count > 2:
        count = 0
        return "I hope I give you the shits"
    else:
        return "Yes"

@Bot.event
async def on_message(message):
    msg = message.content.lower()
    if "no" in msg:
        await Bot.send_message(message.channel, sayYes())
    if "hello" in msg:
        await Bot.send_message(message.channel, sayShutUp())
    
Bot.run("NDUxMDM0ODI1OTQ4OTIxODU2.De8FTQ.V_YAZ1YYSvw4C1iBw5T8CHefRGc")
