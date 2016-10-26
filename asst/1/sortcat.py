import string

def sortcat(num, *strings):
	"""sorts list of strings from longest to shortest"""
	sorted_args = sorted(strings, key=lambda arg: len(arg), reverse=True)

	"""concatenates the first num longest strings, or all of them if num == -1"""
	final_str = ""
	if num == -1:
		for index in xrange(len(strings)):
			final_str += sorted_args[index]
	else:
		for index in xrange(num):
			final_str += sorted_args[index]

	return final_str