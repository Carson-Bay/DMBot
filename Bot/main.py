import os
import discord
from dotenv import load_dotenv
from commands import VC_connection, ping


# Dictionary of commands
commands = {
    "join": VC_connection.join,
    "leave": VC_connection.leave,
    "ping": ping.ping
}

# Change to check what prefix is stored in server object <--------------------
prefix = "$"

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith(prefix):
        command_string = ctx.content.split(" ")[0][len(prefix):].lower()

        if command_string in commands:
            await commands[command_string](ctx, client)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    client.run("ODEyNTE5MzcwODY5NTcxNjA1.YDB7oQ.1wQamKSmDJYDsHpKxS8uPNSf-ZQ")
