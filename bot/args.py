import re

# This is a fairly liberal parser. Any errors like missing quotes will mostly be ignored.
def parse_args(args):
	parsed = []
	index = 0
	inner = False
	while index < len(args):
		prev = index
		index = args.find('"', index + 1)

		chunk = args[prev:index].replace('"', '')
		if inner:
			parsed.append(chunk)
		else:
			split = re.split("\s", chunk.strip())
			for s in split:
				parsed.append(s)
		
		inner = not inner
		if index < 0:
			break

	return parsed

if __name__ == "__main__":
	# TEST
	s = 'This is a "test. The stuff in quotes" should not get split.'
	s = parse_args(s)
	print(s)

	s = 'This is another "test. It should probably result in some error.'
	s = parse_args(s)
	print(s)

	s = 'This should also error!"'
	s = parse_args(s)
	print(s)

	s = 'And yet another " error.'
	s = parse_args(s)
	print(s)