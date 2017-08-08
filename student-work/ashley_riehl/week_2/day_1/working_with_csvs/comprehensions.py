#please add any of the toy examples you build with comprehensions here

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

# make a list of all fish with a for loop
fish_list = []
for fish in fish_tuple:
    if fish != 'octopus':
        fish_list.append(fish)
# print(fish_list)

# make a list of all fish using a list comp
fish_list = [fish for fish in fish_tuple if fish != 'octopus']
# print(fish_list)

# nesting conditionals
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)

list_nums = [1, 2, 3]

# multiply each nummber in a list by 3
times_three = [(num * 3) for num in list_nums]
print(times_three)
