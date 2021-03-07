async def create(args, context, state):
	channel = context.channel
	return await channel.send("Received character create command with args {0}".format(args))

async def list(args, context, state):
	channel = context.channel
	return await channel.send("Received character list command with args {0}".format(args))


async def show(args, context, state):
	channel = context.channel
	return await channel.send("Received character show command with args {0}".format(args))


async def delete(args, context, state):
	channel = context.channel
	return await channel.send("Received character delete command with args {0}".format(args))


async def revive(args, context, state):
	channel = context.channel
	return await channel.send("Received character revive command with args {0}".format(args))
