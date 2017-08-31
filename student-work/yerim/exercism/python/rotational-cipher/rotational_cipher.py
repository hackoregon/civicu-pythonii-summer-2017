import string

def rotate(input, rot):
    alphabet = string.ascii_lowercase
    output = ''
    for letter in input:
        if letter.isalpha() and letter.islower():
            idx = alphabet.index(letter)
            new_idx = (idx + rot) % 26
            output = '{}{}'.format(output, alphabet[new_idx])
        elif letter.isalpha() and letter.isupper():
            idx = alphabet.index(letter.lower())
            new_idx = (idx + rot) % 26
            print(letter, new_idx)
            output = '{}{}'.format(output, alphabet[new_idx].upper())
        else:
            output = '{}{}'.format(output, letter)

    return output
