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
    song_there = os.path.isfile(r"C:\Users\user\Desktop\discord bot\song.mp4")
    try:
        if song_there:
            os.remove(r"C:\Users\user\Desktop\discord bot\song.mp4")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
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
    t=yt.streams.filter(only_audio=True)
    t[0].download(r"C:\Users\user\Desktop\discord bot")
    await ctx.send("Playing : "+str(url))
    for file in os.listdir("./"):
        if file.endswith(".mp4"):
            os.rename(file, r"C:\Users\user\Desktop\discord bot\song.mp4")
    voice.play(discord.FFmpegPCMAudio("song.mp4"))
    

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


bot.run(token)
