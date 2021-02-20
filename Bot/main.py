import os
import discord
import pickle
from dotenv import load_dotenv
from classes import Guild, User, Session
from commands import embedMessage, ping, utils, dice


# Persistent data commands
async def change_prefix(ctx: discord.Message, client: discord.Client):

    args = utils.parse(ctx.content)

    if len(args) != 2:
        return await ctx.channel.send("Prefix is not valid")

    else:
        guilds[ctx.guild.id].change_prefix(args[1])
        prefixes[ctx.guild.id] = args[1]
        with open("prefix.pickle", 'wb') as file:
            pickle.dump(prefixes, file)

        return await ctx.channel.send("Prefix has been changed to {}".format(args[1]))


async def create_character(ctx: discord.Message, client: discord.Client):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send("# START CHARACTER CREATION")

    user_characters[ctx.author.id] = User(ctx.author.id, ["#CHARACTER SHEET OBJECT"])
    with open("characters.pickle", "wb") as file:
        pickle.dump(user_characters, file)


# Session commands
async def session_manager(ctx: discord.Message, client: discord.Client):
    args = utils.parse(ctx.content)

    if args[1] == "start":
        return await start_session(ctx, client)
    elif args[1] == "end":
        return await end_session(ctx, client)
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


async def end_session(ctx: discord.Message, client: discord.Client):
    guild_id = ctx.guild.id
    try:
        if sessions[guild_id] is None:
            return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))
    except KeyError:
        return await ctx.channel.send(embed=embedMessage.create("Session", "You don't have a session in progress", "red"))

    sessions[guild_id] = None
    return await ctx.channel.send(embed=embedMessage.create("Session", "Your session has concluded", "blue"))


# Dictionary of commands
commands = {
    "ping": ping.ping,
    "changeprefix": change_prefix,
    "createcahracter": create_character,
    "session": session_manager,
    "roll": dice.roll_dice
}

# Initializations
guilds = {}  # Dictionary of Server objects (Initialized at start)
prefixes = {}  # Dictionary of prefixes keyed by server ID (pickled)
sessions = {}  # Dictionary of active sessions keyed by server ID
user_characters = {}  # Dictionary of character sheets keyed by user ID (pickled)

default_prefix = "$"
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    # Load prefix preferences
    try:
        with open("prefix.pickle", "rb") as file:
            prefixes = pickle.load(file)
    except FileNotFoundError:
        print("Prefix file not found")

    # Load User Characters
    try:
        with open("characters.pickle", "rb") as file:
            user_characters = pickle.load(file)
    except FileNotFoundError:
        print("Character file not found")

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
