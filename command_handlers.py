import random
from embeds import create_error, create_embed
from commands import lookup as lookup_commands, character as character_commands, session as session_commands, combat as combat_commands

async def echo(args, context, state):
	channel = context.channel
	if len(args) != 1:
		return await channel.send(embed = create_error("Usage: echo [message]. Hint: You may need to put quotes around your message."))
	
	message = args[0]
	return await channel.send(message)

async def character(args, context, state):
	COMMANDS = {
		"create": character_commands.create,
		"list": character_commands.list,
		"show": character_commands.show,
		"delete": character_commands.delete,
		"revive": character_commands.revive,
	}

	if len(args) < 1:
		return await context.channel.send(embed=create_error("A sub-command must be specified."))

	try:
		command = COMMANDS[args[0]]
		return await command(args[1:], context, state)
	except KeyError:
		return await context.channel.send(embed=create_error("Command {0} does not exist.".format(args[0])))

async def session(args, context, state):
	COMMANDS = {
		"start": session_commands.start,
		"add": session_commands.add,
		"list": session_commands.list,
		"end": session_commands.end,
	}

	if len(args) < 1:
		return await context.channel.send(embed=create_error("A sub-command must be specified."))

	try:
		command = COMMANDS[args[0]]
		return await command(args[1:], context, state)
	except KeyError:
		return await context.channel.send(embed=create_error("Command {0} does not exist.".format(args[0])))

async def combat(args, context, state):
	COMMANDS = {
		"start": combat_commands.start,
		"damage": combat_commands.damage,
		"end": combat_commands.end,
	}

	if len(args) < 1:
		return await context.channel.send(embed=create_error("A sub-command must be specified."))

	try:
		command = COMMANDS[args[0]]
		return await command(args[1:], context, state)
	except KeyError:
		return await context.channel.send(embed=create_error("Command {0} does not exist.".format(args[0])))

async def lookup(args, context, state):
	COMMANDS = {
		"monster": lookup_commands.monster
	}

	if len(args) < 1:
		return await context.channel.send(embed = create_error("A sub-command must be specified."))

	try:
		command = COMMANDS[args[0]]
		return await command(args[1:], context, state)
	except KeyError:
		return await context.channel.send(embed = create_error("Command {0} does not exist.".format(args[0])))

async def help(args, context, state):
	channel = context.channel
	# We don't care about the arguments.
	return await channel.send(embed=create_embed("Help", "http://dungeonmaster.tech/documentation.html", "orange"))
