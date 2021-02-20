import discord
from Bot.commands.embedMessage import *


async def ping(ctx: discord.Message, client: discord.Client):
    await ctx.channel.send(embed=create("Pong", "", "green"))
