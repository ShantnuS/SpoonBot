######################
#### SpoonBot 0.1 ####
######################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import config

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
    if count == 3:
        return "I hope I give you the shits"
    elif count == 5:
        count = 0
        return "Well, come on, you beauties!"
    else:
        return "Yes"

def getHelpEmbed():
    embed = discord.Embed(title="Come and have a go, if you think you're hard enough!", description="HELP:", color=0x00ff00)
    return embed
    

@Bot.event
async def on_message(message):
    msg = message.content.lower()
    if "no" in msg:
        await Bot.send_message(message.channel, sayYes())
    if "hello" in msg:
        await Bot.send_message(message.channel, sayShutUp())
    if "what" in msg:
        await Bot.send_file(message.channel, 'images\\spoon_attack.jpg')
    if "!help" in msg:
        await Bot.send_message(message.author, embed=getHelpEmbed())
    
Bot.run(config.BOT_TOKEN)
