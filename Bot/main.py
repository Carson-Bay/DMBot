import os
import discord
import pickle
from dotenv import load_dotenv
from classes import Guild, User, Session
from character import Character, CharacterCompletion
from commands import embedMessage, ping, utils, dice

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


# ----------Persistent data commands----------
async def change_prefix(ctx: discord.Message, client: discord.Client):

    args = utils.parse(ctx.content)

    if len(args) != 2:
        return await ctx.channel.send("Prefix is not valid")

    else:
        guilds[ctx.guild.id].change_prefix(args[1])
        prefixes[ctx.guild.id] = args[1]
        with open(os.path.join(__location__, "prefix.pickle"), 'wb') as file:
            pickle.dump(prefixes, file)

        return await ctx.channel.send("Prefix has been changed to {}".format(args[1]))

# ----------character commands----------
async def character_command_manager(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)

    if args[1] == "create":
        return await create_character(ctx, client)
    elif args[1] == "show":
        return await show_character(ctx, client)
    elif args[1] == "add":
        return await character_add_item(ctx, client)
    elif args[1] == "delete":
        return await character_delete(ctx, client)
    elif args[1] == "revive":
        return await character_revive(ctx, client)
    elif args[1] == "characterlist":
        return await character_list(ctx, client)
    else:
        return await ctx.channel.send(embed=embedMessage.create("Character", "Not a valid character command", "red"))


async def create_character(ctx: discord.Message, client: discord.Client):
    dm_channel = await ctx.author.create_dm()
    if ctx.author.id not in user_characters:
        user_characters[ctx.author.id] = User(ctx.author.id, [])
    elif len(user_characters[ctx.author.id].character) != 0 and user_characters[ctx.author.id].character[len(user_characters[ctx.author.id].character) - 1].creation_progress != CharacterCompletion.FINISH:
        return await ctx.channel.send(embed=embedMessage.create("Warning!", "There is already a character in the process of creation, please finish or cancel the character first!", "red"))
    
    new_character = Character()
    await dm_channel.send("Starting character creation process.\nThis process can be terminated at any time with \"exit\" or \"cancel\".")
    await dm_channel.send(new_character.current_message)

    user_characters[ctx.author.id].add_char_sheet(new_character)

    with open(os.path.join(__location__, "characters.pickle"), "wb") as file:
        pickle.dump(user_characters, file)





async def show_character(ctx: discord.Message, client: discord.Client):

    # Show a single character sheet based off its name
    user_id = ctx.author.id
    args = utils.parse(ctx.content)
    try:
        if user_characters[user_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("You have no characters to show", "Make one using $character create", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("You have no characters to show", "Make one using $character create", "red"))
    else:
        #check if user has this character
        message = ''
        for c in user_characters[user_id].characters:
            if c.name.lower() == args[2].lower():
                message = str(c)
        if len(message) == 0:
            await ctx.channel.send(
                ctx.channel.send(embed=embedMessage.create('you do not have this character', 'Try making it using $character create', 'red')))
        else:
            ctx.channel.send(embed=embedMessage.create('Character Sheet', message,  'blue'))


async def character_list(ctx: discord.Message, client: discord.Client):

    # Show list of names of a user's characters

    user_id = ctx.author.id

    args = utils.parse(ctx.content)

    try:
        if user_characters[user_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("You don't have any characters to show", "Try creating one with $character create", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("You don't have any characters to show", "Try creating one with $character create", "red"))

    else:
        # Add all the characters ot the str
        message = ''

        for c in user_characters[user_id].characters:
            message += c.name + ', '

        # remove the final ,
        message = message[:-2]

        ctx.channel.send(embed=embedMessage.create("User's Characters", message, 'blue'))



async def character_add_item(ctx: discord.Message, client: discord.Client):
    pass


async def character_delete(ctx: discord.Message, client: discord.Client):
    pass


async def character_revive(ctx: discord.Message, client: discord.Client):
    pass


# ----------Combat commands----------
async def combat_command_manager(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)

    if args[1] == "start":
        return await start_combat(ctx, client)
    elif args[1] == "damage":
        return await damage_in_combat(ctx, client)
    else:
        return await ctx.channel.send(embed=embedMessage.create("Combat", "Not a valid combat command", "red"))


async def start_combat(ctx: discord.Message, client: discord.Client):
    pass


async def damage_in_combat(ctx: discord.Message, client: discord.Client):
    pass


# ----------Session commands----------
async def session_command_manager(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)

    if args[1] == "start":
        return await start_session(ctx, client)
    elif args[1] == "end":
        return await end_session(ctx, client)
    elif args[1] == "add":
        return await add_to_session(ctx, client)
    elif args[1] == "session_list":
        return await session_list(ctx, client)
    else:
        return await ctx.channel.send(embed=embedMessage.create("Session", "Not valid session command", "red"))


async def start_session(ctx: discord.Message, client: discord.Client):
    guild_id = ctx.guild.id
    try:
        if sessions[guild_id] is not None:
            return await ctx.channel.send(embed=embedMessage.create("Session", "You already have a session in progress", "red"))
    except KeyError:
        pass

    session = Session(guild_id)
    sessions[guild_id] = session
    return await ctx.channel.send(embed=embedMessage.create("Session", "Your session has begun", "blue"))


async def add_to_session(ctx: discord.Message, client: discord.Client):

    #add character to session

    guild_id = ctx.guild.id
    user_id = ctx.author.id
    args = utils.parse(ctx.content)

    try:
        if sessions[guild_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))

        if user_characters[user_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("You have no characters to show", "Make one using $character create", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("You have no characters to show", "Make one using $character create", "red"))
    # check if user has that character
    character = None
    for c in user_characters[user_id].characters:
        if c.name == args[2]:
            character = c
    if character is None:
        await ctx.channel.send(embed=embedMessage.create('you do not have this character', 'Try making it using $character create','red'))
    else:
        sessions[guild_id].characters.append(character)
        ctx.channel.send(embed=embedMessage.create('Session', 'Character Added', 'blue'))


async def end_session(ctx: discord.Message, client: discord.Client):
    guild_id = ctx.guild.id
    try:
        if sessions[guild_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))

    sessions[guild_id] = None
    return await ctx.channel.send(embed=embedMessage.create("Session", "Your session has concluded", "blue"))


async def session_list(ctx: discord.Message, client: discord.Client):

    # Uses session dict to find all the characters in the session and shows each character name one after the other

    guild_id = ctx.guild.id

    args = utils.parse(ctx.content)

    try:
        if sessions[guild_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))

    else:
        # Add all the characters ot the str
        message = ''

        for c in sessions[guild_id].characters:
            message += c.name + ', '

        # remove the final ,
        message = message[:-2]

        ctx.channel.send(embed=embedMessage.create('Characters in Session', message, 'blue'))


# ----------Lookup Functions----------
async def lookup_command_manager(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)
    if len(args) != 3 and len(args) != 2:
        return await ctx.channel.send(embed=embedMessage.create("Lookup Error", "Missing arguments", "red"))

    if args[1] == "monster":
        await monster_lookup(ctx, client)
    else:
        await ctx.channel.send(embed=embedMessage.create("Lookup Error", "Invalid lookup type", "red"))


async def monster_lookup(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)
    if len(args) != 3:
        return await ctx.channel.send(embed=embedMessage.create("Monster Error", "Incorrect Arguments\n"
                                                                                 "*You may need to put quotes around monster name*", "red"))

    # Load monsters
    try:
        with open(os.path.join(__location__, "monsters.pickle"), "rb") as file:
            monsters = pickle.load(file)
    except FileNotFoundError:
        print("Monster file not found")

    else:
        for key in monsters.keys():
            if key.lower() == args[2].lower():
                monster_data = monsters[key]
                return await ctx.channel.send(embed=embedMessage.create("{}".format(key),
                                                                        "--------------------------\n"
                                                                        "**Type**: {0}\n"
                                                                        "**Size**: {1}\n"
                                                                        "**Alignment**: {2}\n"
                                                                        "**CR**: {3}\n"
                                                                        "**XP**: {4}\n"
                                                                        "**Tags**: {5}"
                                                                        "".format(monster_data["type"],
                                                                                  monster_data["size"],
                                                                                  monster_data["align"],
                                                                                  monster_data["cr"],
                                                                                  monster_data["xp"],
                                                                                  monster_data["tags"]), "green"))

        return await ctx.channel.send(embed=embedMessage.create("Monster Error", "Monster {} not found\n"
                                                                                 "*You may need to put quotes around monster name*".format(args[2]), "red"))


# Dictionary of commands
commands = {
    "ping": ping.ping,
    "changeprefix": change_prefix,
    "character": character_command_manager,
    "session": session_command_manager,
    "roll": dice.roll_dice,
    "lookup": lookup_command_manager
}

# Initializations
guilds = {}  # Dictionary of Server objects (Initialized at start)
prefixes = {}  # Dictionary of prefixes keyed by server ID (pickled)
sessions = {}  # Dictionary of active sessions keyed by server ID
monsters = {}  # Dictionary of monster data (pickled)
user_characters = {}  # Dictionary of character sheets keyed by user ID (pickled)

default_prefix = "$"
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Load prefix preferences
    try:
        with open(os.path.join(__location__, "prefix.pickle"), "rb") as file:
            prefixes = pickle.load(file)
    except FileNotFoundError:
        print("Prefix file not found")

    # Load User Characters
    try:
        with open(os.path.join(__location__, "characters.pickle"), "rb") as file:
            user_characters = pickle.load(file)
    except FileNotFoundError:
        print("Character file not found")

    # Load monsters
    try:
        with open(os.path.join(__location__, "monsters.pickle"), "rb") as file:
            monsters = pickle.load(file)
    except FileNotFoundError:
        print("Monster file not found")

    for guild in client.guilds:
        try:
            prefix = prefixes[guild.id]
        except KeyError:
            prefix = default_prefix
        guilds[guild.id] = Guild(guild.id, prefix)


@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.guild is None:
        if user_characters[ctx.author.id] is None or len(user_characters[ctx.author.id].character) == 0:
            return
        current_character = user_characters[ctx.author.id].character.pop()
        if current_character.creation_progress != CharacterCompletion.FINISH:
            output = current_character.continue_create(ctx.content)
            dm_channel = await ctx.author.create_dm()
            await dm_channel.send(output)
            if output != "Character creation has been cancelled.":
                user_characters[ctx.author.id].character.append(current_character)
        return

    try:
        prefix = guilds[ctx.guild.id].prefix
    except KeyError:
        prefix = default_prefix

    if ctx.content.startswith(prefix):
        command_string = ctx.content.split(" ")[0][len(prefix):].lower()

        if command_string in commands:
            await commands[command_string](ctx, client)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    client.run(TOKEN)
