import json
import os

WORKING_DIR = os.getcwd()

def save_dict(name, dict):
	jstr = json.dumps(dict)
	write(name + ".json", jstr)

def load_dict(name):
	jstr = read(name + ".json")
	if jstr == None:
		return {}
	else:
		dict = json.loads(jstr)
		return dict

def write(name, data):
	save_file = os.path.join(WORKING_DIR, name)
	with open(save_file, "w") as file:
		file.write(data)

def read(name):
	save_file = os.path.join(WORKING_DIR, name)
	try:
		with open(save_file, "r") as file:
			data = file.read()
			return data
	except FileNotFoundError:
		print("Failed to read file {0}, returning None.".format(save_file))
		return None
