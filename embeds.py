from discord import Embed, Colour

COLOURS = {
	"red": Colour.red(),
	"orange": Colour.orange(),
	"yellow": Colour.gold(),
	"green": Colour.green(),
	"blue": Colour.blue(),
	"purple": Colour.purple(),
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