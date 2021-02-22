async def echo(args, context, state):
	channel = context.channel
	if len(args) != 1:
		return await channel.send("Usage: echo [message]. Hint: You may need to put quotes around your message.")
	
	message = args[0]
	return await channel.send(message)
