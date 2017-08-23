def is_isogram(phrase):
    phrase = phrase.lower()

    for char in [' ', '-']:
        phrase = phrase.replace(char, '')
    
    #phrase_list = [letter for letter in phrase] - not necessary
    phrase_set = {letter for letter in phrase} 

    # A set would not allow duplicate letters, therefore its length will be
    # not equal to the list length.
    if len(phrase) == len(phrase_set):
        return True
    else:
        return False
