import bluesclues
abbrev = bluesclues.get_abbrev()
def bluesbooze(state_lookup):
	for state_code, state in abbrev.iteritems():
		if state == state_lookup:
			return state_code