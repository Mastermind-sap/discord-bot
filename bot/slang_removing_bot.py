import discord
import requests
token = open("token.txt", "r").read()
client = discord.Client()

def check_profanity(text):
	obj = requests.get('http://www.wdylike.appspot.com/?q=' + str(text))
	if 'true' in obj.text:
		return True
	elif 'false' in obj.text:
		return False
		
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if check_profanity(message.content):
        await message.channel.purge(limit=1)
        await message.channel.send('NO BAD WORDS HERE!')

client.run(token)
