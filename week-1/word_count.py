#First way to count a string
def word_count(sentence):
        my_string = sentence.split()
        
        #print(my_string)
        
        my_dict = {}
        for word in my_string:
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1
        return my_dict

print(word_count("whatcha whatcha want whatcha want"))

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
