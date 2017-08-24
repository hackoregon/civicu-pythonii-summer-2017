import string

def prep_string(sentence):
    #strip out non white space punctuation and replace with white space
    for char in string.punctuation:
        sentence = sentence.replace(char, " ")
    return sentence.split()


def word_count(sample):
    
    process_sample = prep_string(sample)
   # print(process_sample)
    count = {}
    for word in process_sample:
     #   print(word)
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1
            
    return count


#test_sample = "one fish two fish red fish blue fish"

#print(word_count(test_sample))
 
