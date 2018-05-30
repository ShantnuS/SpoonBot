######################
#### SpoonBot 0.1 ####
#### By ShantnuS #####
######################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import config

#######################################
#   _____ _____   ____   ____  _   _  #
#  / ____|  __ \ / __ \ / __ \| \ | | #
# | (___ | |__) | |  | | |  | |  \| | #
#  \___ \|  ___/| |  | | |  | | . ` | #
#  ____) | |    | |__| | |__| | |\  | #
# |_____/|_|     \____/ \____/|_| \_| #
####################################### 

#Ready the client
Bot = commands.Bot(command_prefix='', case_insensitive=True)

#Global variables
no_count = 0

#Ready event
@Bot.event
async def on_ready():
    print("I'm ready! My name: " + Bot.user.name + " and my ID: " + Bot.user.id)

#Scenario specific responses 
def sayShutUp():
    return "Shut Up"

def sayYes():
    global no_count
    no_count += 1
    if no_count == 3:
        return "I hope I give you the shits"
    elif no_count == 5:
        no_count = 0
        return "Well, come on, you beauties!"
    else:
        return "Yes"

def getHelpEmbed():
    embed = discord.Embed(title="Come and have a go, if you think you're hard enough!", description="HELP:", color=0x00ff00)
    embed.add_field(name="Hello", value="Shut Up", inline=False)
    embed.add_field(name="No", value="Yes", inline=False)
    return embed
    
#On message event
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
    
#config.py contains a BOT_TOKEN variable that is the token from the discord developer website. 
#This token is needed to run the bot. Replace with your own token to run your bot. 
Bot.run(config.BOT_TOKEN)
