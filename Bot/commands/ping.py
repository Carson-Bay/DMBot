import discord


async def ping(ctx: discord.Message, client: discord.Client):
    await ctx.channel.send("Pong")
