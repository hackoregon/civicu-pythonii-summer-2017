import re

def word_count(string):

    string = string.replace(',', ' ').replace('_', ' ').replace('.', ' ')
    string = string.lower()
    # lst = string.split()

    lst = re.findall(r"[\w']+", string)

    unique = set(lst)
    word_dict = dict.fromkeys(unique, 0)

    for word in lst:
        if word in lst:
            word_dict[word] += 1

    # for k in word_dict:
    #     print str(k) + ': ' + str(word_dict[k])

    return word_dict
