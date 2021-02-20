import discord
from Bot.commands.utils import *
from Bot.commands.embedMessage import *
import random


async def roll_dice(ctx: discord.Message, client: discord.Client):
    args = parse(ctx.content)

    if len(args) == 2 or len(args) == 3:
        numdice = 1  # Default num dice
        darg = args[1]  # Where the "d.." will be if no amount is specified
        if darg.isnumeric() and len(args) == 3:
            # An amount of dice is specified
            numdice = int(darg)
            darg = args[2]

        if numdice < 1 or numdice > 999:
            await ctx.channel.send(embed=create('Invalid number of dice', 'min 1, max 999.', 'red'))
            return

        # At this point, numdice and dargs are properly set
        if not darg[0] == "d":
            await ctx.channel.send(embed=create("Error rolling dice", "Format: `roll <amount=1> d[sides]`\nExample: $roll 5 d20",'red'))
            return

        if not darg[1:].isnumeric():
            await ctx.channel.send(embed=create("Dice sides must be a number", '', 'red'))
            return

        sides = int(darg[1:])
        if sides < 2 or sides > 999:
            await ctx.channel.send(embed=create("Invalid number of sides", " min 2, max 999", 'red'))
            return
        num_str = 'You rolled '
        num_list = []

        for i in range(1, numdice + 1):
            num_list.append(random.randint(1, sides))
        for n in num_list[:-1]:
            num_str += str(n) + ', '

        num_str += 'and ' + str(num_list[-1])

        num_str += '\nFor a total sum of ' + str(sum(num_list))

        # if just one num, no need for extra stuff, easier to override at the end
        if numdice == 1:
            num_str = 'You rolled a ' + str(num_list[0])

        await ctx.channel.send(embed=create('Dice Rolls', num_str, 'blue'))

    else:
        await ctx.channel.send(embed=create("Error rolling dice", "Format: `roll <amount=1> d[sides]`\nExample: $roll 5 d20", 'red'))


