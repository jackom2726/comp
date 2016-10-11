import string
import collections

def swapchars(str_input):

    """creates a string with only the inputted string's letters"""
    str_letters = "".join(c for c in str_input if c in (string.letters))

    """finds the most and least common letters"""
    freq_list = collections.Counter(str_letters.lower()).most_common()
    most_freq = freq_list[0][0]
    least_freq = freq_list[-1][0]

    """switches least and most common letters"""
    str_list = list(str_input)
    for index in xrange(len(str_input)):
        if str_list[index].lower() == most_freq:
            if str_list[index].isupper():
                str_list[index] = least_freq.upper()
            else:
                str_list[index] = least_freq
        elif str_list[index].lower() == least_freq:
            if str_list[index].isupper():
                str_list[index] = most_freq.upper()
            else:
                str_list[index] = most_freq
                  
    return ("".join(str_list))


def sortcat(num, *strings):

	"""sorts list of strings from longest to shortest"""
	sorted_args = sorted(strings, key=lambda arg: len(arg), reverse=True)

	"""concatenates the first num longest strings, or all of them if num == -1"""
	final_str = ""
	if num == -1:
		for index in xrange(len(strings)):
			final_str += sorted_args[index]
	else:
		for inde1x in xrange(num):
			final_str += sorted_args[index]

	return final_str


"""creates dictionary of states and statecodes"""
abbrev = {}
infile = open("states.txt", "r")
for line in infile:
	abbrev[line.split(",")[1][:-1]] = line.split(",")[0]


"""looks up the state for a give state code"""
def bluesclues(state_code):
	return abbrev[state_code]


"""looks up the state code for a give state"""
def bluesbooze(state_lookup):
	for state_code, state in abbrev.iteritems():
		if state == state_lookup:
			return state_code