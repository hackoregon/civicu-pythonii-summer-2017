#Written in PyCharm 2017.2, Python 3.5.

def isogram(word):
    if isinstance(word,str):
        w = word.lower()
        return word, len(w) == len(set(w)) if w else False
    else:
        raise TypeError('Argument should be a string')

def is_isogram(string):
    unique_letters = {letter for letter in string}
    if len(unique_letters) == len(string):
        return (string, True)
    else:
        return(string, False)


print(is_isogram("eleven"))
print(isogram("eleven"))





