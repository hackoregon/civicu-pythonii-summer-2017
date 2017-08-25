import collections
import string


def word_count(sentence):
    noPunctuation = ""
    for char in sentence:
        if char not in string.punctuation: #removes punctuation
            noPunctuation += char
        else:
            noPunctuation += " "
    words = noPunctuation.lower().split()
    result = collections.Counter(words) #keeps track of how many times equivalent values are added
    return(result)



'''
#Second way to count a string using regex and dict
import re

dict = {}
sentence_list = ['This is Cassandra Delieto', 'This is Cassandra']
for sentence in sentence_list:
    for word in re.split('\s', sentence): # split with whitespace
        try:
            dict[word] += 1
        except KeyError:
            dict[word] = 1
print(dict)
'''