import re

def parse_args(args):
	parsed = re.split('\s+(?=(?:[^\'"]*[\'"][^\'"]*[\'"])*[^\'"]*$)', args)
	for i in range(0, len(parsed)):
		parsed[i] = parsed[i].replace('"', '').replace("'", "")
	return parsed

if __name__ == "__main__":
	# TEST
	s = 'This is a "test. The stuff in quotes" should not get split.'
	s = parse_args(s)
	print(s)