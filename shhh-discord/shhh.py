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

def common_member(a):
        f=open(r"bannedwords.txt","r")
        a_set = set(a)
        b_set = set(f.read().split("\n"))
        f.close()
        if (a_set & b_set):
                return True
        else:
                return False		

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        
        if (check_profanity(message.content) or common_member(message.content.lower().split())) and (not (message.content.lower().startswith("!ban"))):
                await message.channel.purge(limit=1)
                await message.channel.send('NO BAD WORDS HERE!')
                
        if message.content.lower().startswith("!ban"):
                f=open(r"bannedwords.txt","a+")
                s=message.content.lower()[4::].strip()+"\n"
                data=f.read().split("\n")
                print(data)
                print(s[:-1:])
                if (" " not in (s)) and (s[:-1:] not in data):
                        f.write(s)
                        f.close()
                        await message.channel.purge(limit=1)
                        await message.channel.send("BANNED THE WORD SUCCESSFULLY!")
                elif s[:-1:] in data:
                        await message.channel.purge(limit=1)
                        await message.channel.send("WORD IS ALREADY BANNED!")
                        f.close()
                else:
                        await message.channel.send('CAN BAN WORDS ONLY!')
                        f.close()

client.run(token)
