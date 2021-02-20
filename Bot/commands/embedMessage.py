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


# adds image to passed in embed
def add_image(embed_msg: discord.embeds.Embed, url: str):
    embed_msg.set_image(url=url)

