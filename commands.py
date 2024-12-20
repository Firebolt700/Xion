"""
commands.py - Class to hold and organize all of Xion's commands/events using the discord module's commands.Cog class

Started on: 2024-11-11

Written by Firebolt

"It's just a few keystrokes. Easy, right?" - Squall "Leon" Leonhart to the tech illiterate native tropical islander Sora

"""

### Import stuff
import discord
import src.functions as XionFunctions
from discord.ext import commands


### XionCommands
# Class to hold and organize all of Xion's commands/events instead of everything being in one main file
class XionCommands(commands.Cog):
    # Initialize commands cog object and assign bot property
    def __init__(self, bot):
        self.bot = bot

    # Listener for when messages are sent in servers Xion is in
    @commands.Cog.listener()
    async def on_message(self, message):
        # Xion, don't read your own messages
        if message.author == self.bot.user:
            return

        # Process the command if the message starts with command prefix, otherwise see if message matches quote-response dictionary
        if not message.content.startswith(self.bot.command_prefix):
            await message.channel.send(XionFunctions.pick_response(message=message))

    # Cool embedded message command to print out all of the members of Organization XIII and some details about each of them in a pretty looking way
    @commands.command(
        name="orgxiii",
        help="Lists members of Organization XIII, the element they control, and type of Nobody they command.",
    )
    async def org_xiii(self, ctx):
        # Create Organization XIII list using Discord embedded message
        org_xiii_embed = discord.Embed(
            title="Organization XIII",
            description="Seeking to complete Kingdom Hearts and become whole",
            color=0x808080,  # 808080 - Hex code for the color grey
        )

        org_xiii_embed.add_field(
            name="I. Xemnas",
            value="AKA Ansem (Xehanort), power over **Nothingness**, commands **Sorcerers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="II. Xigbar",
            value="AKA Braig, power over **Space**, commands **Snipers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="III. Xaldin",
            value="AKA Dilan, power over **Wind**, commands **Dragoons**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="IV. Vexen",
            value="AKA Even, power over **Ice**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="V. Lexaeus",
            value="AKA Aeleus, power over **Earth**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="VI. Zexion",
            value="AKA Ienzo, power over **Illusions**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="VII. Saix",
            value="AKA Isa, power over the **Moon**, commands **Berserkers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="VIII. Axel",
            value="AKA Lea, power over **Fire**, commands **Assassins**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="IX. Demyx",
            value="Power over ***DANCE WATER DANCE***, commands **Dancers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="X. Luxord",
            value="Power over **Time**, commands **Gamblers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="XI. Marluxia",
            value="AKA Lauriam, power over **Flowers**, commands **Reapers**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="XII. Larxene",
            value="AKA Elrena, power over **Lightning**, commands **Ninjas**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="XIII. Roxas",
            value="AKA Sora, power over **Light** and **Sticks**, commands **Samurai**",
            inline=False,
        )
        org_xiii_embed.add_field(
            name="XIV. Xion",
            value="AKA Replica No. i, power over **Light**",
            inline=False,
        )

        # Send generated Org XIII list as embedded message
        await ctx.send(embed=org_xiii_embed)

    # Searches the KH wiki for an entered term, has to match the format of the KH Wiki URL format
    @commands.command(
        name="khwiki",
        help="Searches for a specific term on the KH Wiki and sends the link to the webpage",
    )
    async def kh_wiki(self, ctx, *target):
        await ctx.send(XionFunctions.get_kh_wiki_link(target))

    # Takes any name/word and turns into a Nobody styled name similar to the names of the Organization XIII members
    @commands.command(
        name="nobodyname",
        help="Takes a word/name and Nobody-izes it (shuffles the letters and adds an X)",
    )
    async def nobody_name(self, ctx, target):
        # Send Nobody name
        await ctx.send(XionFunctions.get_nobody_name(target))

    # Picks a random quote from Kingdom Hearts and sends it to the chat
    @commands.command(
        name="khquote",
        help="Picks a random meme quote from Kingdom Hearts and sends it to the chat",
    )
    async def kh_quote(self, ctx):
        # Send randomly chosen quote
        await ctx.send(XionFunctions.get_random_kh_quote())

    # Rolls various sided dice, mostly meant for DND purposes
    @commands.command(
        name="roll", help="Rolls any number of multi-sided die and displays all results"
    )
    async def roll(self, ctx, *dice):
        # Get dice roll result and send to chat
        await ctx.send(XionFunctions.get_dice_roll(dice))
