import string

def word_count(input):
    counts = dict()
    phrase = input.replace('_', ' ').replace(',', ' ').replace('.', ' ').lower()
    exclude = set(string.punctuation)
    phrase = ''.join(p for p in phrase if p not in exclude)
    word_list = phrase.split()

    for word in word_list:
        counts[word] = counts.get(word,0) + 1
    return counts
