from basic_objects import *
import discord

def parse(content):
    return content.split()

async def add_track(ctx: discord.Message, client: discord.Client):
    ctx = parse(ctx)

    track_items = [] # things in track like instrument instance


    #-------------------------- add to master list of tracks in server instance

    # add to track_items #possibly use pop to check the 0th entry every time
    i = 1
    while i < len(ctx):

        pass








async def del_track(ctx: discord.Message, client: discord.Client):
    #delete track

    pass


async def add_sleep(ctx: discord.Message, client: discord.Client):
    # add sleep to track


    pass


async def show(ctx: discord.Message, client: discord.Client):
    # show all objects to user


    pass