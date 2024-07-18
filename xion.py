# xion.py
import os

import discord
import datetime
import random
from random import shuffle
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

#Add command prefixes -- DONE
bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has entered the Round Room. Praise Kingdom Hearts.')
    
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

		

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'I\'ll use this instead!':
        response = 'Roxas, that\'s a stick.'
        await send_message(message.channel,response)

    if message.content == 'Who am I supposed to eat ice cream with?':
        response = 'What the fuck is wrong with u'
        await send_message(message.channel,response)
    
    if message.content.casefold() == 'Skibidi Toilet'.casefold():
        response = ':skull: you\'re going straight to Kingdom Hearts for that one'
        await send_message(message.channel,response)

    '''if message.author.id == 305783441943953419:
        await message.delete()
        response = 'To the Realm of Darkness with your bullshit.'
        await message.channel.send(response)'''
    

    await bot.process_commands(message)

@bot.event
async def send_message(channel, message):
    await channel.send(message)
    

''' DOES NOT WORK - MUDAE CANT READ COMMANDS FROM OTHER BOTS
mudaeRollTimes = [datetime.time(0,10),
                 datetime.time(1,10),
                 datetime.time(2,10),
                 datetime.time(3,10),
                 datetime.time(4,10),
                 datetime.time(5,10),
                 datetime.time(6,10),
                 datetime.time(7,10),
                 datetime.time(8,10),
                 datetime.time(9,10),
                 datetime.time(10,10),
                 datetime.time(11,10),
                 datetime.time(12,10),
                 datetime.time(13,10),
                 datetime.time(14,10),
                 datetime.time(15,10),
                 datetime.time(16,10),
                 datetime.time(17,10),
                 datetime.time(18,10),
                 datetime.time(19,10),
                 datetime.time(20,10),
                 datetime.time(21,10),
                 datetime.time(22,10),
                 datetime.time(23,10),
                 datetime.time(12,50)]

for rollTime in mudaeRollTimes:
     print(rollTime)

@tasks.loop(time=mudaeRollTimes)
async def mudae_rolls():
    mudaeChannel = bot.get_channel(1216546351081328671)
    print('Running mudae rolls...')
    await mudaeChannel.send('Free community rolls!')
    await mudaeChannel.send('$m')'''


@bot.command(name='orgXIII', help='Lists members of Organization XIII, the element they control, and type of Nobody they command.')
async def orgXIII(ctx):
    orgXIIIList = [
        'Xemnas AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**',
        'Xigbar AKA Braig, power over **Space**, commands **Snipers**',
        'Xaldin AKA Dilan, power over **Wind**, commands **Dragoons**',
        'Vexen AKA Even, power over **Ice**',
        'Lexaeus AKA Aeleus, power over **Earth**',
        'Zexion AKA Ienzo, power over **Illusions**',
        'Saix AKA Isa, power over the **Moon**, commands **Berserkers**',
        'Axel AKA Lea, power over **Fire**, commands **Assassins**',
        'Demyx, power over ***DANCE WATER DANCE***, commands **Dancers**',
        'Luxord, power over **Time**, commands **Gamblers**',
        'Marluxia AKA Lauriam, power over **Flowers**, commands **Reapers**',
        'Larxene AKA Elrena, power over **Lightning**, commands **Ninjas**',
        'Roxas AKA Sora, power over **Light**, commands **Samurai**',
        'Xion AKA Replica No. i, power over **Light**'
    ]

    message = ''

    for orgXIIIMember in orgXIIIList:
        message += orgXIIIMember + '\n'

    await ctx.send(message)

@bot.command(name='khwiki', help='Searches for a specific term on the KH Wiki and sends the link to the webpage')
async def khwiki(ctx, *target):
    if target is None or target == '':
        await ctx.send('Please specify a term to search for on the KH Wiki.')
        return
    
    khWikiLink = 'https://www.khwiki.com/'
    
    target = '_'.join(target)

    khWikiLink += target

    await ctx.send(khWikiLink)

@bot.command(name='nobodyname', help='Takes a word/name and Nobody-izes it (shuffles the letters and adds an X)')
async def nobody_name(ctx, target):
    if target is None or target == '':
        await ctx.send('Please specify a word or name to create a Nobody name.')
        return
    
    # Choose a random spot to place the added X
    randomCharIndex = random.randint(0, len(target))

    # Create the Nobody name
    nobodyName = list(target) # initially create name as list of input string
    nobodyName.insert(randomCharIndex, 'x') # add the letter X to a random spot in the list
    shuffle(nobodyName) # shuffle the list contents
    nobodyName = ''.join(nobodyName) # re-join the characters from the list as a string

    # Make all characters in the name lowercase...
    nobodyName = nobodyName.lower()
    # ...then capitalize the first letter to make it look like a name
    nobodyName = nobodyName.capitalize()

    # Send Nobody name
    await ctx.send('Your Nobody name is ' + nobodyName)
        

bot.run(TOKEN)