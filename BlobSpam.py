import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

blobs = ['<:lennyblob:420025593971736576>','<:killerblob:421158118131499020>','<:blobzipmouth:420026864350789632>','<:blobwaitwhat:420025888374128650>','<:blobunamused:420026857233186816>','<:blobsuspect:424704698210320395>','<:blobstop:420025585020960770>','<:blobsob:420325706510368788>','<:blobscream:420026602747985930>','<:blobscared:420196151816355840>','<:blobpeek:422160492648202250>','<:blobpatrol:420025878844801064>','<:blobok:420025865821487104>','<:blobnom:420325619709116438>','<:blobninja:420025707054366722>','<:blobnarrowedeye:420351346814746624>','<:blobmelt:420325593289195531>','<:blobhurt:420026693781291018>','<:blobhmm:420026644346961930>','<:blobgrinning:420026359084220417>','<:blobfacepalm:420025697638154240>','<:blobexpressionless:420026349210828811>','<:blobdrool:420325054186913793>','<:blobdizzy:420026341413355520>','<:blobdevil:420325712214622208>','<:blobcry2:420026330147586058>','<:blobaww:420025399058235392>','<:blobangry3:420026098290786305>','<:blobangel:420026090506158082>']

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
        print(userID)
        args = message.content.split(" ")
        
        if int(args[1]) <= 25:
            val = int(args[1])
        else:
            val = 25
        for i in range(val):
            time.sleep(1)
            if userID == '207963869895852032':
                await client.send_message(message.channel, 'Oh its only you' )
                await client.send_message(message.channel, blobs[16])
            elif userID == '418599237501059072':
                await client.send_message(message.channel, 'You have made a grave enemy' )
                await client.send_message(message.channel, blobs[1])
            else:
                await client.send_message(message.channel, blobs[random.randint(0,28)])
            

client.run("NDMyMjM4MDU4NTA3ODYyMDM3.DaqaDA.QaN3-bnd2H6rFbUog5J85axfGyQ")
