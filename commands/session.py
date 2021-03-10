async def start(args, context, state):
	channel = context.channel
	return await channel.send("Received session start command with args {0}".format(args))

async def add(args, context, state):
	channel = context.channel
	return await channel.send("Received session add command with args {0}".format(args))


async def list(args, context, state):
	channel = context.channel
	return await channel.send("Received session list command with args {0}".format(args))


async def end(args, context, state):
	channel = context.channel
	return await channel.send("Received session end command with args {0}".format(args))
