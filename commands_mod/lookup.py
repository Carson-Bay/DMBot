async def monster(args, context, state):
	channel = context.channel
	return await channel.send("Received lookup monster command with args {0}".format(args))
