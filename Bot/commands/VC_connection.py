import discord


async def join(ctx: discord.Message, client: discord.Client):
    channel = ctx.author.voice.channel
    await channel.connect()


async def leave(ctx: discord.Message, client: discord.Client):
    for x in client.voice_clients:
        if x.guild == ctx.guild:
            return await x.disconnect()
    await ctx.channel.send("I am not connected to any voice channel on this server!")
