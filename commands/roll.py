from embeds import create_error, create_embed
import random

async def roll(args, context, state):
	ARGUMENT_ERROR = "Improper arguments. Usage: roll <amount=1> d[sides]"

	channel = context.channel
	if len(args) > 2 or len(args) < 1:
		return await channel.send(embed=create_error(ARGUMENT_ERROR))

	amount = 1
	darg = args[0]
	if args[0].isnumeric():
		amount = int(args[0])
		darg = args[1]

	if amount < 1 or amount > 10:
		return await channel.send(embed=create_error("Amount of dice must be between 1 and 10."))

	if not darg.startswith("d") or not darg[1:].isnumeric():
		return await channel.send(embed=create_error(ARGUMENT_ERROR))

	sides = int(darg[1:])

	if sides < 2 or sides > 999:
		return await channel.send(embed=create_error("Sides must be between 2 and 999."))

	rolls = []
	for _ in range(0, amount):
		roll = random.randint(1, sides)
		rolls.append(roll)

	mrolls = str(rolls[0])
	for i in range(1, len(rolls)):
		mrolls += ", {0}".format(rolls[i])

	message = "You rolled {0}\nSum: {1}".format(mrolls, sum(rolls))
	return await channel.send(embed=create_embed("Roll", message, "blue"))
