import discord
from discord.ext import commands,tasks

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

bot = commands.Bot(command_prefix='!joker ')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def join(ctx):
    channel=ctx.message.author.voice.channel
    await channel.connect()
    
##@bot.command()
##async def play(ctx):
##    channel=ctx.message.author.voice.channel
##    vc=await channel.connect()
##    vc.play(discord.FFmpegPCMAudio('bhai.mp3'), after=lambda e: print('done', e))
##    await ctx.send('Now playing')

@bot.command()
async def play(ctx, *, query):
    """Plays a file from the local filesystem"""
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(query))

@bot.command()
async def leave(ctx):
    await Voicedisconnect()
    
bot.run(token)
