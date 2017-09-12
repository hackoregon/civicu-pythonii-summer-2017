import re
import string

def rotate(thing, rotate):
    letters = list(string.ascii_lowercase)

    answer = []
    for letter in thing:
        if letter.lower() in letters:
            upper = False
            if letter.isupper():
                upper = True
            letter = letter.lower()
            rot_val = letters.index(letter)
            value = (rot_val + rotate) % 26
            if upper:
                rotated = letters[value].upper()
            else:
                rotated = letters[value]
            answer.append(rotated)
        else:
            answer.append(letter)

    return ''.join(answer)
