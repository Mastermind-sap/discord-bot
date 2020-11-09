##incompleted yt tuitorial


##import discord
##import json
##import asyncio
##import youtube_dl
##import shell
##import os
##from discord.utils import get
##from discord.ext import commands
##
##@client.command(pass_context=True)
##async def join(ctx):
##    global voice
##    channel=ctx.message.author.voice.channel
##    voice=get(client.voice_clients,guild=ctx.guild)
##
##    if voice and voice.is_connected():
##        await voice.move_to(channel)
##    else:
##        voice=await chqannel.connect()
##    await ctx.send(f"Joined {channel}")
##
##@client.command(pass_context=True)
##async def leave(ctx):
##    channel=ctx.message.author.voice.channel
##    voice=get(client.voice_clients,guild=ctx.guild)
##
##    if voice and voice.is_connected():
##        await voice.disconnect()
##        await ctx.send(f"Left {channel}")
##
##@client.command(pass_context=True,aliases=["p"])
##async def play(ctx,url:str):
##    def check_queue():
##        Queue_infile=os.path.indir("./Queue")
##        if Queue_infile is True:
##            DIR =os.path.abspath(os.path.realpath("Queue"))
##            length=len(os.
##            
