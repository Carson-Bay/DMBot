import discord


def parse(content):
    return content.split()


async def start_dm(ctx: discord.Message, client: discord.Client):
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send("hello")


async def respond(ctx: discord.Message, client: discord.Client):
    channel = ctx.channel
    await channel.send("hello")

def is_positive_input(str):
    return str == "y" or str == "yes"