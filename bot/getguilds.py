import discord
from discord.ext import commands,tasks
token = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='!joker ')


async def is_it_me(ctx):
    if(str(ctx.author.id) == mainaccid):
        await ctx.send("HELLO MASTERMIND")
        return True
    else:
        await ctx.send("ONLY MASTERMIND(owner of the bot) CAN USE THIS COMMAND")
        return False

@bot.command()
async def server(ctx):
    name=str(ctx.guild.name)
    description=str(ctx.guild.description)
    owner=str(ctx.guild.owner)
    _id = str(ctx.guild.id)
    region=str(ctx.guild.region)
    memcount=str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed=discord.Embed(
        title=name +" Server Information",
        description=description,
        color=discord.Color.blue()
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner",value=owner,inline=True)
    embed.add_field(name="Server Id",value=_id,inline=True)
    embed.add_field(name="Region",value=region,inline=True)
    embed.add_field(name="Member Count",value=memcount,inline=True)

    await ctx.send(embed=embed)

@commands.check(is_it_me)
@bot.command()
async def servers(ctx):
    activeservers = bot.guilds
    for guild in activeservers:
        name=str(guild.name)
        description=str(guild.description)
        owner=str(guild.owner)
        _id = str(guild.id)
        region=str(guild.region)
        memcount=str(guild.member_count)
        icon = str(guild.icon_url)

        embed=discord.Embed(
                title=name +" Server Information",
                description=description,
                color=discord.Color.blue()
                )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner",value=owner,inline=True)
        embed.add_field(name="Server Id",value=_id,inline=True)
        embed.add_field(name="Region",value=region,inline=True)
        embed.add_field(name="Member Count",value=memcount,inline=True)

        await ctx.send(embed=embed)
        print(guild.name)

@commands.check(is_it_me)
@bot.command()
async def msgservers(ctx,*,text):
    activeservers = bot.guilds
    for guild in activeservers:
        for channel in guild.channels:
            if('general' in channel.name.lower()):
                try:
                    await channel.send(text)
                    await ctx.send("Sent message to Guild: "+guild.name+" Channel: "+channel.name)
                except Exception as e:
                    await ctx.send(e)
bot.run(token)
