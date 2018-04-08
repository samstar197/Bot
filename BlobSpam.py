import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

blobs = [':eyes:',':lennyblob:',':killerblob:',':blobzipmouth:',':blobwaitwhat:',':blobunamused:',':blobsuspect:',':blobstop:',':blobsob:',':blobscream:',':blobscared:',':blobpeek:',':blobpatrol:',':blobok:',':blobnom:',':blobninja:',':blobnarrowedeye:',':blobmelt:',':blobhurt:',':blobhmm:',':blobgrinning:',':blobfacepalm:',':blobexpressionless:',':blobdrool:',':blobdizzy:',':blobdevil:',':blobcry2:',':blobaww:',':blobangry3:',':blobangel:']

Client = discord.Client()
client = commands.Bot(command_prefix = ">:)")



@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith(">:)"):
        userID = message.author.id
        await client.send_message(message.channel, 'as you wish <@%s>' %(userID))
        for i in range(25):
            print('in loop')
            time.sleep(1)
            await client.send_message(message.channel, blobs[random.randint(0,28)])
            

client.run("NDMyMjM4MDU4NTA3ODYyMDM3.DaqaDA.QaN3-bnd2H6rFbUog5J85axfGyQ")
