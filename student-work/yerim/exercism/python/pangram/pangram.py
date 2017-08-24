from collections import Counter

def is_pangram(sentence):
    sentence.lower()

    # remove all on-alphabets
    alphastr = ''.join(filter(str.isalpha, sentence))

    counter = Counter(alphastr)

    if len(counter.keys()) == 26:
        return True
    else:
        return False
