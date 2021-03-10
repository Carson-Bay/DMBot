import re

# This is a fairly liberal parser. Any errors like missing quotes will mostly be ignored.
def parse_args(args):
	parsed = []
	index = 0
	inner = False
	while index < len(args):
		prev = index
		index = args.find('"', index + 1)
		chunk = args[prev:index]
		if index < 0:
			chunk = args[prev:]
		
		if inner:
			chunk = chunk[1:]
			if chunk: # Ensure chunk is not empty
				parsed.append(chunk)
		else:
			for s in re.split("\s", chunk.strip().replace('"', '')):
				if s: # Ensure s is not empty
					parsed.append(s)
		
		inner = not inner
		if index < 0:
			break

	return parsed