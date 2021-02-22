from discord import Embed

COLOURS = {
	"red": 0xff0000,
	"orange": 0xffa500,
	"yellow": 0xffff00,
	"green": 0x008000,
	"blue": 0x0000ff,
	"purple": 0xab00ff
}

# Input colour as either a hex code or a name string
def get_colour(colour):
	try:
		return COLOURS[colour]
	except KeyError:
		return colour

def create_embed(title, content, colour):
	colour = get_colour(colour)
	return Embed(title = title, description = content, color = colour)

def create_error(content):
	return create_embed("Error", content, "red")