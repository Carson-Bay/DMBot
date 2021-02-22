import discord
import os
from dotenv import load_dotenv

import commands
from state import State
from args import parse_args
from embeds import create_embed

COMMANDS = {
	"echo": commands.echo
}

client = discord.Client()
state = None

def main():
	global state

	load_dotenv() # Loads the .env file. Vars can be retrieved via os.getenv("NAME")
	token = os.getenv("TOKEN")
	state = State(client)
	client.run(token)

@client.event
async def on_ready():
	print("Logged in as {0}".format(client.user))

@client.event
async def on_message(message):
	if message.author == client.user:
		return # Don't respond to messages sent by ourselves

	content = message.content
	prefix = state.get_prefix(message.guild)
	if not content.startswith(prefix):
		return # Make sure the prefix matches

	content = content[len(prefix):] # Remove prefix from content
	args = parse_args(content)
	try:
		command = args[0].lower()
		command = COMMANDS[command]
		await command(args[1:], message, state)
	except KeyError:
		channel = message.channel
		return await channel.send(embed = create_embed("Error", "Command does not exist.", "red"))

if __name__ == "__main__":
	main()