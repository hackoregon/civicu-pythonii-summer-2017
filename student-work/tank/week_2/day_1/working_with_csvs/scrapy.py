bicycle_sent = 'a blue bicycle'

# get a list of all letters with a for loop
bicycle_letters = []
for letter in bicycle_sent:
    bicycle_letters.append(letter)

# get all letters with a list comp
bicycle_letters = [letter for letter in bicycle_sent]
print(bicycle_letters)

my_dict = {"a": 1, "b": 2, "c": 3}

# using a for loop
flipped_dict = {}
for key, value in my_dict.items():
    flipped_dict[value] = key
print(flipped_dict)