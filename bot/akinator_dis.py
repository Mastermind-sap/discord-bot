import discord
from discord.ext import commands,tasks
import akinator as ak

token = open("token.txt", "r").read()
mainaccid=open("mainaccid.txt", "r").read()

bot = commands.Bot(command_prefix='!joker ')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(aliases=["aki"])
async def akinator(ctx):
    await ctx.send("Akinator is here to guess!")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b"]
    try:
        aki = ak.Akinator()
        q = aki.start_game()
        while aki.progression <= 80:
            await ctx.send(q)
            await ctx.send("Your answer:(y/n/p/b)")
            msg = await bot.wait_for("message", check=check)
            if msg.content.lower() == "b":
                try:
                    q=aki.back()
                except ak.CantGoBackAnyFurther:
                    await ctx.send(e)
                    continue
            else:
                try:
                    q = aki.answer(msg.content.lower())
                except ak.InvalidAnswerError as e:
                    await ctx.send(e)
                    continue
        aki.win()
        await ctx.send(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?(y/n)\n{aki.first_guess['absolute_picture_path']}\n\t")
        correct = await bot.wait_for("message", check=check)
        if correct.content.lower() == "y":
            await ctx.send("Yay\n")
        else:
            await ctx.send("Oof\n")
    except Exception as e:
        await ctx.send(e)


bot.run(token)
