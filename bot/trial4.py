import discord
import random
from discord.ext import commands,tasks
from itertools import cycle
import pyjokes
import joke_generator

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

bot = commands.Bot(command_prefix='!joker ')
bot.remove_command("help")
status=cycle(["Why So Sad!?","JOKER IS HERE","Use !joker"])

@bot.command(pass_context=True)
async def help(ctx):
    author=ctx.message.author
    help_embed=discord.Embed(title="Joker Help",description="Use !joker before any command",color=discord.Colour.red())
    help_embed.set_thumbnail(url=bot.user.avatar_url)
    help_embed.add_field(name="mention",value="mentions a user",inline=False)
    help_embed.add_field(name="whois/info/details",value="returns details of mentioned user",inline=False)
    help_embed.add_field(name="getdp/getprofilepic/dp",value="returns the profile pic of mentioned user",inline=False)
    help_embed.add_field(name="pm/dm/pvtmessage",value="sends private message to mentioned user",inline=False)
    help_embed.add_field(name="clean/clear",value="one with managing messages permission can delete n number of msgs from a channel",inline=False)
    help_embed.add_field(name="hi/hello",value="say hi",inline=False)
    help_embed.add_field(name="uthere/areuthere",value="ask are you there",inline=False)
    help_embed.add_field(name="insult",value="insult someone",inline=False)
    help_embed.add_field(name="goodnight/goodn8/nightynight",value="wish goodnight",inline=False)
    help_embed.add_field(name="bye/sayonara/adios",value="say bye",inline=False)
    help_embed.add_field(name="spam",value="spam some text n number of times",inline=False)
    help_embed.add_field(name="choice/choose/select/random",value="choose random item from a list",inline=False)
    help_embed.add_field(name="ping",value="display the ping",inline=False)
    help_embed.add_field(name="cjoke/coding_joke",value="crack a coding related joke",inline=False)
    help_embed.add_field(name="joke",value="crack a joke",inline=False)
    help_embed.set_footer(text="Requested by: "+str(author))
    await author.send(embed=help_embed)
    
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
async def mention(ctx, user : discord.Member):
  await ctx.send(user.mention)

@bot.command(aliases=["info","details"])
async def whois(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    embed=discord.Embed(title=member.name,description=member.mention,color=discord.Colour.red())
    embed.add_field(name="ID",value=member.id,inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command(aliases=["getprofilepic","dp"])
async def getdp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)

##@bot.command(aliases=["memeify"])
##@commands.check(is_it_me)
##async def meme(ctx, member: discord.Member = None):
##    if not member:
##        member = ctx.author

        
@bot.command(aliases=["dm","pvtmessage"])
async def pm(ctx , member: discord.Member = None,*,text):
    if not member:
        member = ctx.author
    await member.send(text)

@bot.command(aliases=["clean"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

@bot.command(aliases=["hi"])
async def hello(ctx, user : discord.Member):
     await ctx.send('Hello! '+user.mention, file=discord.File('hello.gif'))

@bot.command(aliases=["uthere"])
async def areuthere(ctx, user : discord.Member):
     await ctx.send('Are You There? '+user.mention, file=discord.File('areuthere'+str(random.randint(1,3))+'.gif'))

@bot.command()
async def insult(ctx, user : discord.Member):
    await ctx.send('Insulting'+user.mention,file=discord.File('insult'+str(random.randint(1,4))+'.gif'))

@bot.command(aliases=["goodn8","nightynight"])
async def goodnight(ctx, user : discord.Member):
    await ctx.send('Good Night! '+user.mention,file=discord.File('gn.gif'))

@bot.command(aliases=["sayonara","adios"])
async def bye(ctx, user : discord.Member):
    await ctx.send('Bye! '+user.mention,file=discord.File('bye.gif'))

@bot.command()
async def spam(ctx, times,*,text):
    for i in range(int(times)):
        await ctx.send(text)

@bot.command(aliases=["choose","select","random"])
async def choice(ctx,options="yes ,no"):
    await ctx.send(random.choice(options.split(",")))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency *1000)}ms')

@bot.command(aliases=["cjoke"])
async def coding_joke(ctx):
    await ctx.send(pyjokes.get_joke())

@bot.command()
async def joke(ctx):
    await ctx.send(joke_generator.generate())


bot.run(token)
