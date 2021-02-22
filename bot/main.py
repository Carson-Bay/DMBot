import discord
import os
from dotenv import load_dotenv

client = discord.Client()

def main():
	load_dotenv() # Loads the .env file. Vars can be retrieved via os.getenv("NAME")
	token = os.getenv("TOKEN")
	client.run(token)

@client.event
async def on_ready():
	print("Logged in as {0}".format(client.user))

@client.event
async def on_message(message):
	if message.author == client.user:
		return # Don't respond to messages sent by ourselves
	
	if message.content.lower().startswith("$echo "):
		await message.channel.send(message.content[len("$echo "):])

if __name__ == "__main__":
	main()