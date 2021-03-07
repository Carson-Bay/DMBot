import random
from embeds import create_error, create_embed
from commands_mod import lookup as lookup_commands
from commands_mod import character as character_commands
from commands_mod import session as session_commands

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
	channel = context.channel
	return await channel.send("Received combat command with args {0}".format(args))

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

async def roll(args, context, state):
	ARGUMENT_ERROR = "Improper arguments. Usage: roll <amount=1> d[sides]"

	channel = context.channel
	if len(args) > 2 or len(args) < 1:
		return await channel.send(embed = create_error(ARGUMENT_ERROR))
	
	amount = 1
	darg = args[0]
	if args[0].isnumeric():
		amount = int(args[0])
		darg = args[1]
	
	if amount < 1 or amount > 10:
		return await channel.send(embed = create_error("Amount of dice must be between 1 and 10."))

	if not darg.startswith("d") or not darg[1:].isnumeric():
		return await channel.send(embed = create_error(ARGUMENT_ERROR))
	
	sides = int(darg[1:])
	
	if sides < 2 or sides > 999:
		return await channel.send(embed = create_error("Sides must be between 2 and 999."))
	
	rolls = []
	for _ in range(0, amount):
		roll = random.randint(1, sides)
		rolls.append(roll)

	mrolls = str(rolls[0])
	for i in range(1, len(rolls)):
		mrolls += ", {0}".format(rolls[i])

	message = "You rolled {0}\nSum: {1}".format(mrolls, sum(rolls))
	return await channel.send(embed = create_embed("Roll", message, "blue"))


async def change_prefix(args, context, state):
	channel = context.channel
	
	if len(args) != 1:
		return await channel.send(embed = create_error("Improper arguments. Usage: changeprefix [new_prefix]"))
	
	prefix = args[0]
	if len(prefix) > 1:
		return await channel.send(embed = create_error("Prefix is too long."))
	elif prefix.isalnum(): # Prefix cannot be alphanumeric
		return await channel.send(embed = create_error("Prefix must not be alphanumeric."))
	
	state.set_prefix(context.guild, prefix)
	return await channel.send(embed = create_embed("Success", "Set prefix to {0}".format(prefix), "green"))

async def help(args, context, state):
	channel = context.channel
	# We don't care about the arguments.
	return await channel.send(embed=create_embed("Help", "http://dungeonmaster.tech/documentation.html", "orange"))
