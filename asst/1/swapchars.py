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