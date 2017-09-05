'''
## In-Class Exercise

Create a regular expression that can find all the floating point decimal numbers in a string, like $1000.00 or 1e3 or 1000.0001.
Then coerce that string into a float (so you the dollar sign shouldn't be in your number string).
Write a unittest or doctest that checks 3 numbers in one string.
If that's got you stumped, start with recognizing an integer, then work your way up.
'''

import re

def find_numbers(string):
    match_numbers = re.compile(r'[0-9]*[.e]?[0-9]+')
    numbers = match_numbers.findall(string)

    return [float(x) for x in numbers]

