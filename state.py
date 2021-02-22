DEFAULT_PREFIX = "$"

class State:
	def __init__(self, client):
		self.client = client
		self.prefixes = {} # TODO: Load prefixes from save file
	
	def set_prefix(self, guild, prefix):
		self.prefixes[guild] = prefix
		# TODO: Save prefixes
	
	def get_prefix(self, guild):
		try:
			return self.prefixes[guild]
		except KeyError:
			return DEFAULT_PREFIX