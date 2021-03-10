import savedata

DEFAULT_PREFIX = "$"
PREFIX_NAME = "prefixes"

class State:
	def __init__(self, client):
		self.client = client
		self.prefixes = savedata.load_dict(PREFIX_NAME)
	
	#NOTE: Ensure all keys are strings when getting and setting dictionary data. This is for JSON compatibility.
	def set_prefix(self, guild, prefix):
		key = str(guild.id)
		self.prefixes[key] = prefix
		savedata.save_dict(PREFIX_NAME, self.prefixes)
	
	def get_prefix(self, guild):
		try:
			key = str(guild.id)
			return self.prefixes[key]
		except KeyError:
			return DEFAULT_PREFIX
