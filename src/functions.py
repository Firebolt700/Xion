"""
Xion_Functions.py - Contains custom methods used by Xion that aren't direct bot commands from Xion_Commands

Started on: 2024-12-20

Written by Firebolt

"Don't talk with your mouth full." - Aerith "Shishkebab" Gainsborough to the yapping MCP

"""

### Import stuff
import random

### Variables used for custom functions

# Create list of famous KH quotes that can be added to
# TODO: Add more quotes
kh_quotes = [
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

# Create dictionary (key-value pairs) for hard-coded messages/responses
# Keys must be written in lowercase for check in pick_response() method to work
quote_response_dict = {
    "i can improvise": "Roxas, that's a stick.",
    "who else will i have ice cream with": "What the fuck is wrong with you?",
    "skibidi toilet": ":skull: you're going straight to Kingdom Hearts for that one.",
}

### XionFunctions


# Xion_Commands.on_message()
def pick_response(quote):

    # Compare quote-response dictionary keys to incoming message
    # Requires keys in dictionary to be all lowercase
    lowerQuote = quote.lower()
    # If the message matches a dictionary key
    if lowerQuote in quote_response_dict:
        # Set the key-paired value as the response message and return the value
        return quote_response_dict[lowerQuote]
    # If message does NOT match a dictionary key, return nothing
    else:
        return None


# Xion_Commands.kh_wiki()
# Custom method to get KH Wiki link based on whether or not the normal search using khwiki or synthesis-focused khsynth commands were used
def get_kh_wiki_link(target):
    # Check if a parameter for the command was given or if its null/empty
    if target is None or not target:
        return "Please specify a term to search for on the KH Wiki."

    # Join KH Wiki HTTP link with search query
    kh_wiki_link = "https://www.khwiki.com/" + "_".join(target)

    # Send generated KH Wiki link to appropriate context
    return kh_wiki_link


# Xion_Commands.nobody_name()
# Custom method for taking an inputted name or string and generating a Nobody name version in the same style as Kingdom Hearts Nobody names
def get_nobody_name(target):
    # Check if a parameter for the command was given or if its null/empty
    if target is None or not target:
        return "Please specify a word or name to create a Nobody name."

    # Choose a random spot to place the added X
    random_char_index = random.randint(0, len(target))

    ### Create the Nobody name
    # initially create name as list of input string
    nobody_name = list(target)

    # add the letter X to a random spot in the list
    nobody_name.insert(random_char_index, "x")

    # shuffle the list contents
    random.shuffle(nobody_name)

    # re-join the characters from the list as a string
    nobody_name = "".join(nobody_name)

    # Make all characters in the name lowercase...
    nobody_name = nobody_name.lower()

    # ...then capitalize the first letter to make it look like a name
    nobody_name = nobody_name.capitalize()

    # Return Nobody name
    return "Your Nobody name is " + nobody_name + "."


# Xion_Commands.kh_quote()
# Custom method for getting a random KH quote from a pre-made list
def get_random_kh_quote():
    # Choose random quote out of KH quote list and return choice
    return random.choice(kh_quotes)


# Xion_Commands.roll()
def get_dice_roll(dice):
    # TODO: Currently not working, need a DND brain to figure this out
    return "Dice roll machine broke, come back later."
