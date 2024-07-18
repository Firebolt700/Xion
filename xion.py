# xion.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has entered the Round Room. Praise Kingdom Hearts.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "I'll use this instead!":
        response = 'Roxas, that\'s a stick.'
        await message.channel.send(response)

client.run(TOKEN)