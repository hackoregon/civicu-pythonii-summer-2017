""" 
The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists matches the bin size. 

For example calling the function with a list of names and the size of 2 should return 
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is 
remaining add that name to another inner list.
"""
import random
def names_func(a_list, size):

        random.shuffle(student_list)

        random_student_list = [student_list[i:i + size] for i in range(0, len(student_list), size)]

        if len(random_student_list[-1]) == 1:
            random_student_list[-2].append(random_student_list[-1][0])

            random_student_list.pop()

        return random_student_list

    names_func("bob tom time too tack take week walk elk",2)

    """
    This func should take a list and size, break the list into lists of the
    size and return a list of lists.
    """



if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))

