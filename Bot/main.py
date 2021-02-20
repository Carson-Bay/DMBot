import os
import discord
import pickle
from dotenv import load_dotenv
from commands import ping, utils
from classes import Guild


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


# Dictionary of commands
commands = {
    "ping": ping.ping,
    "changeprefix": change_prefix
}

guilds = {}  # Dictionary of Server objects (Initialized at start)

prefixes = {}

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
        print("file not found")
        prefixes = {}
    for guild in client.guilds:
        try:
            prefix = prefixes[guild.id]
        except KeyError:
            prefix = default_prefix
        guilds[guild.id] = Guild(guild.id, prefix)


@client.event
async def on_message(ctx):
    try:
        prefix = guilds[ctx.guild.id].prefix
    except KeyError:
        prefix = default_prefix

    if ctx.author == client.user:
        return

    if ctx.content.startswith(prefix):
        command_string = ctx.content.split(" ")[0][len(prefix):].lower()

        if command_string in commands:
            await commands[command_string](ctx, client)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    client.run(TOKEN)
