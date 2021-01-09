import discord
from discord.ext import commands
#import youtube_dl
import os
from pytube import YouTube

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()
bot = commands.Bot(command_prefix='!joker ')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def play(ctx, url : str):
##    song_there = os.path.isfile(r"C:\Users\user\Desktop\discord bot\song.mp4")
##    try:
##        if song_there:
##            os.remove(r"C:\Users\user\Desktop\discord bot\song.mp4")
##    except PermissionError:
##        await ctx.send("Wait for the current playing music to end or use the 'stop' command :negative_squared_cross_mark:")
##        return
    try:
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=str(ctx.message.author.voice.channel))
        await voiceChannel.connect()
        await ctx.send("Joined "+str(ctx.message.author.voice.channel)+" voice channel!:white_check_mark:")
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    except AttributeError:
        await ctx.send(ctx.message.author.mention+" is not in any voice channel :negative_squared_cross_mark:")
        return
    except:
        await ctx.send(ctx.message.author.mention+" joker in another voice channel of this server \n Cannot be in two voice channels simultaneously :negative_squared_cross_mark:")
    
##    ydl_opts = {
##        'format': 'bestaudio/best',
##        'postprocessors': [{
##            'key': 'FFmpegExtractAudio',
##            'preferredcodec': 'mp3',
##            'preferredquality': '192',
##        }],
##    }
##    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
##        ydl.download([url])
    yt=YouTube(str(url))
    yt_embed=discord.Embed(title=yt.title+":musical_note:",description=yt.description,color=discord.Colour.red())
    yt_embed.set_thumbnail(url=yt.thumbnail_url)
    yt_embed.add_field(name="Author: ",value=yt.author+":musical_score: ",inline=False)
    yt_embed.add_field(name="Duration: ",value=str(yt.length)+" seconds :clock3: ",inline=False)
    yt_embed.add_field(name="Publish date: ",value=str(yt.publish_date)+":calendar_spiral:",inline=False)
    yt_embed.add_field(name="Rating: ",value=str(yt.rating)+":star2:",inline=False)
    yt_embed.add_field(name="Views: ",value=str(yt.views)+":eyes:",inline=False)
    t=yt.streams.filter(only_audio=True)
    t[0].download(r"C:\Users\user\Desktop\discord bot")
##    for file in os.listdir("./"):
##        if file.endswith(".mp4"):
##            os.rename(file, r"C:\Users\user\Desktop\discord bot\song.mp4")
    voice.play(discord.FFmpegPCMAudio(yt.title+".mp4"))
    await ctx.send("Playing "+yt.title+" :loud_sound:")
    await ctx.send(embed=yt_embed)

@bot.command(aliases=["disconnect","exit"])
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("Disconnected :wave:")
    else:
        await ctx.send("The bot is not connected to a voice channel. :negative_squared_cross_mark:")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused :pause_button:")
    else:
        await ctx.send("Currently no audio is playing. :negative_squared_cross_mark:")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resumed :play_pause: ")
    else:
        await ctx.send("The audio is not paused. :negative_squared_cross_mark:")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Stopped playing :octagonal_sign: ")


bot.run(token)
