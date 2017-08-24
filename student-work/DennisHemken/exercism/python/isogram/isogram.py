def is_isogram(word):
    word = word.lower()
    list_variable = [letter for letter in word if letter != ' ' and letter != '-']
    list_test = []
    isogram = True
    for letter in list_variable:
        if letter not in list_test:
            list_test.append(letter)
        else:
            isogram = False
    
    return isogram
