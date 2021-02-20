import discord
import enum


class DiscordColours(enum.Enum):
    red = discord.Colour.red()
    green = discord.Colour.green()
    blue = discord.Colour.blue()


def create(title_string: str, description_string: str, colour_string: str):
    returnMessage = discord.Embed(
        title=title_string,
        description=description_string,
        colour=DiscordColours[colour_string].value,
    )

    return returnMessage
