#please add any of the toy examples you build with comprehensions here
students = ['Andrew', 'Casey', 'Nate', 'Jordan', 'Jimmy']

student_list = [' '.join(student) for student in students]
# print(student_list)


fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
# print(fish_list)

list_nums = [1,2,3]
times_three = [(num*3) for num in list_nums]
# print(times_three)


word = 'andrew telleria'
unique_letters = {letter for letter in word}
# print(unique_letters)

my_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in my_dict.items()}
# print(flipped_dict)

squares = [x**2 for x in range(10)]
# print(squares)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)

matrix = [
		 [1,2,3,4],
		 [5,6,7,8],
		 [9,10,11,12]
		 ]

print([[row[i] for row in matrix] for i in range(4)])
print(zip(*matrix))