def rotate(string, key):
    alphabet = [chr(letter) for letter in range(ord('a'), ord('z')+1)]
    cipher = alphabet[key:] + alphabet[:key]

    map = dict(zip(alphabet, cipher))

    print(map)
    outstring = ''
    for letter in string:
        if not letter.isalpha():
            outstring += letter
        else:
            if letter.isupper():
                outstring += map[letter.lower()].upper()
            else:
                outstring += map[letter]

    return outstring
