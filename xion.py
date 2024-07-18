# xion.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

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

client.run(TOKEN)