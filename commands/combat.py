async def start(args, context, state):
	channel = context.channel
	return await channel.send("Received combat start command with args {0}".format(args))


async def damage(args, context, state):
	channel = context.channel
	return await channel.send("Received combat damage command with args {0}".format(args))


async def end(args, context, state):
	channel = context.channel
	return await channel.send("Received combat end command with args {0}".format(args))
