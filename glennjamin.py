import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Glennjamin is ready to post some monday missives!')

@client.event
async def on_message(message):
    if ("usm") in message.content:
        await message.channel.send('*ump')
        
client.run('token here')
