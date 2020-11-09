import discord
import random
from discord.ext import commands
token = open("token.txt", "r").read()
client = discord.Client()
bot = commands.Bot(command_prefix='!joker')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#didnot work on bot join
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel)=="general":
            await client.send_message(f"""WELCOME TO THE SERVER {member.mention}""")

##@bot.command()
##async def mention(ctx, user : discord.Member):
##  await ctx.send(user.mention)

@client.event
async def on_message(message):
    #id=client.get_guild()
    channels=["bot-trial","bot-commands"]
    if str(message.channel) in channels:
        if message.author == client.user:
            return

        if message.content.lower().startswith('!joker'):
            print (message.content)
            print(str(message.content.split[2]))
            print(message.author)
            if "hello" in message.content.lower():
               await message.channel.send('Hello! '+message.author.mention, file=discord.File('hello.gif'))
            if "insult" in message.content.lower():
                await message.channel.send('Insulting'+"@"+message.content.rpartition("@")[2], file=discord.File('insult'+str(random.randint(1,4))+'.gif'))
##            if "play" in message.content.lower():
##                vc = await discord.channel()
##                vc.play(discord.FFmpegPCMAudio('bhai.mp3'), after=lambda e: print('done', e))
##                vc.is_playing()
##            if "pause" in message.content.lower():
##                vc.pause()
##            if "resume" in message.content.lower():
##                vc.resume()
##            if "stop" in message.content.lower():
##                vc.stop()
client.run(token)
