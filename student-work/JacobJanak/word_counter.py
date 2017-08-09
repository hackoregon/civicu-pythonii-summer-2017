import collections
import string

def word_count(phrase):
    # Replace punctuation marks with spaces
    noPunctuation = ""
    for char in phrase:
        if char not in string.punctuation:
            noPunctuation += char
        else:
            noPunctuation += " "

    # Split string into array
    words = noPunctuation.lower().split()

    # Convert array to dictionary with quantities
    result = collections.Counter(words)
    
    return(result)
