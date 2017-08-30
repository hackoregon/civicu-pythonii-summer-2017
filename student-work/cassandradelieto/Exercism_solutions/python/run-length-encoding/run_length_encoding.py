from itertools import groupby
#http://www.techrepublic.com/article/run-length-encoding-in-python/


def encode(l):
#   string = l.lower()
#   return [(len(list(group)), name) for name, group in groupby(string)]
#   can't use list comp due to list output and no concatenation of values.


def decode(text):
	if not text:
		return ""
	else:
		char = text[0]
		quantity = text[1]
		return char * int(quantity) + decode(text[2:])

