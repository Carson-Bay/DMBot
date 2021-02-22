from embeds import create_error

async def echo(args, context, state):
	channel = context.channel
	if len(args) != 1:
		return await channel.send(embed = create_error("Usage: echo [message]. Hint: You may need to put quotes around your message."))
	
	message = args[0]
	return await channel.send(message)
