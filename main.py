import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
# client.run(os.getenv('TOKEN'))
client.run('MTA2NDE3MTMxNzA4MDg5MTUzMg.GWw083.IUdVnp_9nCQW2f2YdHNj4kBL130FIHkuZWpxUc')

