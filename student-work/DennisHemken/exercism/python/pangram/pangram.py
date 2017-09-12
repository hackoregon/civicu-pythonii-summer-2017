from string import ascii_lowercase

"""
def prep_string(sentence):
    #set all characters to lower case to avoid miscounts due to capitalization
    sentence = sentence.lower()
    
    #strip out non white space punctuation and replace with white space
    for char in string.punctuation:
        sentence = sentence.replace(char, " ")
    return sentence.split()
"""
def is_pangram(sentence):
   return all(x in sentence.lower() for x in ascii_lowercase )


