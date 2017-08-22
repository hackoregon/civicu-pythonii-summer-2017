import numpy as np


def distance(s1, s2):
    """Hamming distance between two strings (number of unequal characters)

    >>> distance('ABC', 'DEF')
    3
    >>> distance('ABC', 'ABC')
    0
    """
    return np.sum(~(np.array(list(s1)) == np.array(list(s2))))
