def word_count(phrase):
    d_phrase = {}
    lst_phrase = phrase.split()
    for w in lst_phrase:
        if w in d_phrase:
            d_phrase[w] += 1
        else:
            d_phrase.update({w:1})
    return d_phrase
    #for k , v in d_phrase.items():
            #print(f'{k:<4}: {v}')
#word_count('word')