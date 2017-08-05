#please add any of the toy examples you build with comprehensions here
# building a set using a for loop
unique_letters = set()
for letter in word:
    unique_letters.add(letter)
    
# a set comprehension
unique_letters = {letter for letter in word}