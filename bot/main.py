import discord
import os
from dotenv import load_dotenv

from bot import commands
from bot.state import State
from bot.args import parse_args

COMMANDS = {
	"echo": commands.echo
}

state = None

def main():
	load_dotenv() # Loads the .env file. Vars can be retrieved via os.getenv("NAME")
	client = discord.Client()
	token = os.getenv("TOKEN")
	client.run(token)

	state = State(client)

@client.event
async def on_ready():
	client = state.client
	print("Logged in as {0}".format(client.user))

@client.event
async def on_message(message):
	client = state.client
	if message.author == client.user:
		return # Don't respond to messages sent by ourselves

	content = message.content
	prefix = state.get_prefix(message.guild)
	if not content.starts_with(prefix):
		return # Make sure the prefix matches

	args = parse_args(message.content)
	try:
		command = args[0]
		command = COMMANDS[command]
		command(args[1:], message, state)
	except KeyError:
		channel = message.channel
		return await channel.send("Command does not exist.")

if __name__ == "__main__":
	main()