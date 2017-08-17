import string

def word_count(phrase):
    # Initialize our output dict
    wc = dict()

    # Loop over all possible punctuation marks, and replace them in the phrase
    for char in string.punctuation:
        # Replace any punctuation with spaces
        phrase = phrase.replace(char,' ')

    # Fix the case, and divide based on the spaces
    all_words = phrase.lower().split()

    # Grab the unique words in the list
    unique_words = set(all_words)

    # Create a dictionary based on the count of a word in the list
    for unique_word in unique_words:
        wc[unique_word] = all_words.count(unique_word)

    return wc
    
#word_count('hey,my_spacebar_is_broken.')