from embeds import create_embed, create_error

async def change_prefix(args, context, state):
	channel = context.channel

	if len(args) != 1:
		return await channel.send(embed=create_error("Improper arguments. Usage: changeprefix [new_prefix]"))

	prefix = args[0]
	if len(prefix) > 1:
		return await channel.send(embed=create_error("Prefix is too long."))
	elif prefix.isalnum():  # Prefix cannot be alphanumeric
		return await channel.send(embed=create_error("Prefix must not be alphanumeric."))

	state.set_prefix(context.guild, prefix)
	return await channel.send(embed=create_embed("Success", "Set prefix to {0}".format(prefix), "green"))
