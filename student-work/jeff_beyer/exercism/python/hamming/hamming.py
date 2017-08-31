'''
It is found by comparing two DNA strands and counting how many of the
nucleotides are different from their equivalent in the other string.

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

The Hamming distance between these two DNA strands is 7.
'''
def distance(str1, str2):
    # Make sure the strings exist (not empty)
    if not str1 or not str2:
        return 0
    
    # If the lengths don't match, complain!
    if len(str1) != len(str2):
        raise ValueError

    # Pair 'em up.
    match = zip(str1, str2)
    ham_dist = 0

    # Go into each pair, see if they match or not.
    for pair in match:
        if pair[0] != pair[1]:
            ham_dist += 1 
    
    return ham_dist
