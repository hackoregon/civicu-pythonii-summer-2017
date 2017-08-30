import re

regex = re.compile("r'([+-]?(\\d+\\.)?\\d+)$")
regex1 = r'([+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)'
#| (?: \d+ \.? ) )"
#[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )
print(regex.findall("b1000.01g100h100.4h1.0003"))
#floating point values within a string
floats = ("b1000.01g100h100.4h1.0003")
search = re.findall(regex1,floats)

#(?: creates a non-capturing group.
# + one or more of the expressions


print(search)
#this didnt work

