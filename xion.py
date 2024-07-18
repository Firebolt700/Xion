# xion.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
#Add command prefixes
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    onlineMessage = f'{client.user} has entered the Round Room. Praise Kingdom Hearts.'
    print(onlineMessage)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'I\'ll use this instead!':
        response = 'Roxas, that\'s a stick.'
        await message.channel.send(response)

    if message.content == 'Who am I supposed to eat ice cream with?':
        response = 'What the fuck is wrong with u'
        await message.channel.send(response)
    
    '''if message.content == 'Skibidi Toilet':
        response = ':skull:'
        await message.channel.send(response)'''

    '''if message.author.id == 305783441943953419:
        await message.delete()
        response = 'To the Realm of Darkness with your bullshit.'
        await message.channel.send(response)'''

client.run(TOKEN)