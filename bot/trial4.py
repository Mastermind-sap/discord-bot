import discord
import random
from discord.ext import commands,tasks
from itertools import cycle

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

bot = commands.Bot(command_prefix='!joker ')
status=cycle(["Why So Sad!?","JOKER IS HERE","Use !joker"])

def is_it_me(ctx):
    return str(ctx.author.id) == mainaccid

@bot.event
async def on_ready():
    change_status.start()
    print('We have logged in as {0.user}'.format(bot))

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))
    
@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel)=="general":
            await client.send_message(f"""WELCOME TO THE SERVER {member.mention}""")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments!")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Invalid command!")
    
@bot.command()
@commands.check(is_it_me)
async def mention(ctx, user : discord.Member):
  await ctx.send(user.mention)

@bot.command(aliases=["clean"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

@bot.command(aliases=["hi"])
@commands.check(is_it_me)
async def hello(ctx, user : discord.Member):
     await ctx.send('Hello! '+user.mention, file=discord.File('hello.gif'))

@bot.command(aliases=["uthere"])
@commands.check(is_it_me)
async def areuthere(ctx, user : discord.Member):
     await ctx.send('Are You There? '+user.mention, file=discord.File('areuthere'+str(random.randint(1,3))+'.gif'))

@bot.command()
@commands.check(is_it_me)
async def insult(ctx, user : discord.Member):
    await ctx.send('Insulting'+user.mention,file=discord.File('insult'+str(random.randint(1,4))+'.gif'))

@bot.command(aliases=["goodn8","nightynight"])
@commands.check(is_it_me)
async def goodnight(ctx, user : discord.Member):
    await ctx.send('Good Night! '+user.mention,file=discord.File('gn.gif'))

@bot.command(aliases=["sayonara","adios"])
@commands.check(is_it_me)
async def bye(ctx, user : discord.Member):
    await ctx.send('Bye! '+user.mention,file=discord.File('bye.gif'))

@bot.command()
@commands.check(is_it_me)
async def spam(ctx, times,*,text):
    for i in range(int(times)):
        await ctx.send(text)

@bot.command(aliases=["choose","select","random"])
@commands.check(is_it_me)
async def choice(ctx,options="yes ,no"):
    await ctx.send(random.choice(options.split(",")))

@bot.command()
@commands.check(is_it_me)
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency *1000)}ms')


bot.run(token)
