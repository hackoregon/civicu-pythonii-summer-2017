import re

def is_isogram(string):
    string = re.split(' |-', string)
    string = ''.join(string)
    string = string.lower()
    unique_letters = {letter for letter in string}

    if len(unique_letters) == len(string):
        return True
    else:
        return False
