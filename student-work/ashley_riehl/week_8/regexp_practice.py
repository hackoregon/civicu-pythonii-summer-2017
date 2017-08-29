import re

def number_finder(input):
    """Takes a string as input, finds all of the numbers,
    converts them to floating point numbers.
    """
    matcher = re.compile(r'[0-9]+[.e]?[0-9]+\b')
    matches = matcher.findall(input)

    answer = []
    for match in matches:
        answer.append(float(match))
    return answer
