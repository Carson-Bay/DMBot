from embeds import create_error

async def echo(args, context, state):
	channel = context.channel
	if len(args) != 1:
		return await channel.send(embed = create_error("Usage: echo [message]. Hint: You may need to put quotes around your message."))
	
	message = args[0]
	return await channel.send(message)

async def character(args, context, state):
	channel = context.channel
	return await channel.send("Received character command with args {0}".format(args))

async def session(args, context, state):
	channel = context.channel
	return await channel.send("Received session command with args {0}".format(args))

async def combat(args, context, state):
	channel = context.channel
	return await channel.send("Received combat command with args {0}".format(args))

async def lookup(args, context, state):
	channel = context.channel
	return await channel.send("Received lookup command with args {0}".format(args))

async def roll(args, context, state):
	channel = context.channel
	return await channel.send("Received roll command with args {0}".format(args))

async def change_prefix(args, context, state):
	channel = context.channel
	return await channel.send("Received change_prefix command with args {0}".format(args))

async def help(args, context, state):
	channel = context.channel
	return await channel.send("Received help command with args {0}".format(args))
