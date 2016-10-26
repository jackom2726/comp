abbrev = {}
infile = open("states.txt", "r")
for line in infile:
	abbrev[line.split(",")[1][:-1]] = line.split(",")[0]

def bluesclues(state_code):
	return abbrev[state_code]

def get_abbrev():
	return abbrev