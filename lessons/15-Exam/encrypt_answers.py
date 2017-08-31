""" Functions for "encrypting" exam answers

>>> encrypt('Hello')
'URYYB'
"""


def encrypt(s, rot=13):
    """ Encrypt a string with rotation (Ceasar) cypher """
    s = s.upper()
    if not s:
        return s
    return ''.join([chr((ord(c) - ord('A') + rot) % 26 + ord('A')) if 'A' <= c <= 'Z' else c for c in s])


def encrypt_answers(f='answers.txt', encrypter=encrypt):
    """ Encrypt the lines of a text file and output list of the encrypted strings, one for each line """
    answers = []
    with open(f, 'rt') as f:
        while True:
            line = f.readline().strip()
            if not len(line):
                break
            print(line)
            print(encrypt(line))
            answers += [encrypt(line)]
    return answers
