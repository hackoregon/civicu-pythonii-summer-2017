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
    # Shuffle the names
    random.shuffle(a_list)  

    # Init the groups list (expected to be a list of lists)
    groups = list()

    while len(a_list) >= size:
        # Add the first size elements into our groups list, keep doing that
        # until we have less than size elements left
        groups.append(a_list[:size])
        a_list = a_list[size:]

    # If we have not zero elements left, we need to deal with them
    # If it's only one element, add it to the last group
    if len(a_list) == 1:
        groups[-1].append(a_list[0])
    # Otherwise, just make it another group
    elif len(a_list) > 1:
        groups.append(a_list)

    return groups


if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))
