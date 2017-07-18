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
    """
    This func should take a list and size, break the list into lists of the
    size and return a list of lists.
    """
    final_list = []

    while len(a_list) > 0:
        if len(a_list) >= size:
            # randomly sample
            selected = random.sample(a_list, size)

            # add to the final list
            final_list.append(selected)

            # remove from the a_list
            for name in selected:
                a_list.remove(name)

        elif len(a_list) == 1:
            final_list[-1].extend(a_list)
            a_list = []

        else:
            final_list.append(a_list)
            a_list = []


    return final_list


if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    # print(names_func(["one", "two", "three", "four", "five"], 2))
    test_list = list(range(18))
    print(names_func(test_list, 5))
