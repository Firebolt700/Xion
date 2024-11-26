"""
Xion_Commands.py - Class to hold and organize all of Xion's commands/events instead of everything being in one main file

Who else would we have ice cream with?

Started on: 2024-11-11

Written by Firebolt

"It's just a few keystrokes. Easy, right?" - Squall "Leon" Leonhart to the tech illiterate native tropical islander Sora

"""

# Import stuff
import random
from random import shuffle

import discord
from discord.ext import commands


# Class to hold and organize all of Xion's commands/events instead of everything being in one main file
class Xion_Commands(commands.Cog):
    # Initialize commands cog object and assign bot property
    def __init__(self, bot):
        self.bot = bot

    # Listener for when messages are sent in servers Xion is in
    @commands.Cog.listener()
    async def on_message(self, message):
        # Xion, don't read your own messages
        if message.author == self.bot.user:
            return

        # Process the command if the message starts with command prefix, otherwise see if message matches dictionary
        if not message.content.startswith(self.bot.command_prefix):
            # Create dictionary (key-value pairs) for hard-coded messages/responses
            memeMessageDict = {
                "I can improvise": "Roxas, that's a stick.",
                "Who else will I have ice cream with?": "What the fuck is wrong with you?",
                "Skibidi Toilet": ":skull: you're going straight to Kingdom Hearts for that one.",
            }

            # Loop through the meme message dictionary and send the appropriate response/value if the incoming message matches a key
            for key in memeMessageDict:
                if message.content.casefold() == key.casefold():
                    response = memeMessageDict[key]
                    await message.channel.send(response)
                    break

    # Cool embedded message command to print out all of the members of Organization XIII and some details about each of them in a pretty looking way
    @commands.command(
        name="orgxiii",
        help="Lists members of Organization XIII, the element they control, and type of Nobody they command.",
    )
    async def org_xiii(self, ctx):
        # Old stinky way just using text and markup
        """
        orgXIIIList = [
            '### Organization XIII',
            '* I. Xemnas AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**',
            '* II. Xigbar AKA Braig, power over **Space**, commands **Snipers**',
            '* III. Xaldin AKA Dilan, power over **Wind**, commands **Dragoons**',
                '* IV. Vexen AKA Even, power over **Ice**',
                '* V. Lexaeus AKA Aeleus, power over **Earth**',
                '* VI. Zexion AKA Ienzo, power over **Illusions**',
                '* VII. Saix AKA Isa, power over the **Moon**, commands **Berserkers**',
                '* VIII. Axel AKA Lea, power over **Fire**, commands **Assassins**',
                '* IX. Demyx, power over ***DANCE WATER DANCE***, commands **Dancers**',
                '* X. Luxord, power over **Time**, commands **Gamblers**',
                '* XI. Marluxia AKA Lauriam, power over **Flowers**, commands **Reapers**',
                '* XII. Larxene AKA Elrena, power over **Lightning**, commands **Ninjas**',
                '* XIII. Roxas AKA Sora, power over **Light**, commands **Samurai**',
                '* XIV. Xion AKA Replica No. i, power over **Light**'
            ]

            message = ''

            for orgXIIIMember in orgXIIIList:
                message += orgXIIIMember + '\n'

            await ctx.send(message)
        """

        # New cool way using embedded messages
        embedOrgXIII = discord.Embed(
            title="Organization XIII",
            description="Seeking to complete Kingdom Hearts and become whole",
            color=0x808080,
        )  # 808080 - Hex code for the color grey

        embedOrgXIII.add_field(
            name="I. Xemnas",
            value="AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="II. Xigbar",
            value="AKA Braig, power over **Space**, commands **Snipers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="III. Xaldin",
            value="AKA Dilan, power over **Wind**, commands **Dragoons**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="IV. Vexen",
            value="AKA Even, power over **Ice**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="V. Lexaeus",
            value="AKA Aeleus, power over **Earth**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="VI. Zexion",
            value="AKA Ienzo, power over **Illusions**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="VII. Saix",
            value="AKA Isa, power over the **Moon**, commands **Berserkers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="VIII. Axel",
            value="AKA Lea, power over **Fire**, commands **Assassins**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="IX. Demyx",
            value="Power over ***DANCE WATER DANCE***, commands **Dancers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="X. Luxord",
            value="Power over **Time**, commands **Gamblers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="XI. Marluxia",
            value="AKA Lauriam, power over **Flowers**, commands **Reapers**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="XII. Larxene",
            value="AKA Elrena, power over **Lightning**, commands **Ninjas**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="XIII. Roxas",
            value="AKA Sora, power over **Light** and **Sticks**, commands **Samurai**",
            inline=False,
        )
        embedOrgXIII.add_field(
            name="XIV. Xion",
            value="AKA Replica No. i, power over **Light**",
            inline=False,
        )

        await ctx.send(embed=embedOrgXIII)

    # Searches the KH wiki for an entered term, has to match the format of the KH Wiki URL format
    @commands.command(
        name="khwiki",
        help="Searches for a specific term on the KH Wiki and sends the link to the webpage",
    )
    async def kh_wiki(self, ctx, *target):
        # Check if a parameter for the command was given or if its null/empty
        if target is None or not target:
            await ctx.send("Please specify a term to search for on the KH Wiki.")
            return

        # Join KH Wiki HTTP link with search query
        khWikiLink = "https://www.khwiki.com/" + "_".join(target)

        # Send complete link to chat
        await ctx.send(khWikiLink)

    # Takes any name/word and turns into a Nobody styled name similar to the names of the Organization XIII members
    @commands.command(
        name="nobodyname",
        help="Takes a word/name and Nobody-izes it (shuffles the letters and adds an X)",
    )
    async def nobody_name(self, ctx, target):
        # Check if a parameter for the command was given or if its null/empty
        if target is None or not target:
            await ctx.send("Please specify a word or name to create a Nobody name.")
            return

        # Choose a random spot to place the added X
        randomCharIndex = random.randint(0, len(target))

        ### Create the Nobody name
        # initially create name as list of input string
        nobodyName = list(target)

        # add the letter X to a random spot in the list
        nobodyName.insert(randomCharIndex, "x")

        # shuffle the list contents
        shuffle(nobodyName)

        # re-join the characters from the list as a string
        nobodyName = "".join(nobodyName)

        # Make all characters in the name lowercase...
        nobodyName = nobodyName.lower()

        # ...then capitalize the first letter to make it look like a name
        nobodyName = nobodyName.capitalize()

        # Send Nobody name
        await ctx.send("Your Nobody name is " + nobodyName + ".")

    # Picks a random quote from Kingdom Hearts and sends it to the chat
    @commands.command(
        name="khquote",
        help="Picks a random meme quote from Kingdom Hearts and sends it to the chat",
    )
    async def kh_quote(self, ctx):
        # TODO: Add more quotes
        # Create list of quotes that can be added to
        quoteLibrary = [
            "I'll get him.",
            "Say, fellas, did somebody mention the Door to Darkness?",
            "I know now, without a doubt, Kingdom Hearts... is light!",
            "Dance, water, dance!",
            "I have some unfinished business with this puppet.",
            "You're stupid!",
            "Got it memorized?",
            "As if!",
            "You see, darkness is the heart's true essence.",
            "Can you spare a heart?",
            "No wonder no one wants to die.",
            "And not just the _____. The word _____. They stole it too!",
            '"I\'m me", he says.',
            "Who else will I have ice cream with?",
            "Kairi's... Kairi's inside me?",
            "Your pain shall be twofold!",
            "CHEEEEEEEEEEEeeeeeeeeuuuuhhh....",
            "That didn't take long. Did it break again?",
            "Come, Guardian!",
            "*Donald death sound*",
            "They'll pay for this.",
            "He's got bugs in him!",
            "A faithful Replica, until the very end. That's... okay.",
            "*&&X%",
        ]

        # Send randomly chosen quote
        await ctx.send(random.choice(quoteLibrary))

    # TODO: Fix this garbage
    # Rolls various sided dice, mostly meant for DND purposes
    @commands.command(
        name="roll", help="Rolls any number of multi-sided die and displays all results"
    )
    async def roll(self, ctx, *dice):
        # TODO: Currently not working, need a DND brain to figure this out
        await ctx.send("Dice roll machine broke, come back later.")
        """ Dice roll machine broke
            currentRolls = []
            finalRolls = [[]]
            finalResults = []

            # Loop through dice array
            for die in dice:
                
                # Separate roll modifiers
                numberOfRolls = die.split('d')[0]
                sidedDie = die.split('d')[1]

                # Check to make sure the roll modifier numbers were grabbed correctly
                if numberOfRolls is None or numberOfRolls == '' or not numberOfRolls.isdigit():
                    numberOfRolls = 1

                if sidedDie is None or sidedDie == '' or not sidedDie.isdigit():
                    await ctx.send(commandErrorMessage)
                    return
                
                # Do the rolls based on the number of rolls specified and the number of sides on the die
                for roll in range(numberOfRolls):
                    roll = random.randint(1, int(sidedDie))
                    currentRolls.append(roll)

                finalRolls.append(currentRolls)

            # Add up the results of the rolls and prepare to display them   
            for rollSet in finalRolls:
                results = ''

                for roll in rollSet:
                    results += ' + '.join(str(roll))

                results += " = " + str(sum(rollSet)) + "\n\n"
                finalResults.append(results)

            finalMessage = 'Roll results: \n\n'

            for result in finalResults:
                finalMessage += result

            await ctx.send(finalMessage)
            """
