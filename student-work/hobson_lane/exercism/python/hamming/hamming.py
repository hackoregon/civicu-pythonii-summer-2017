import numpy as np


def distance(s1, s2):
    """ Hamming distance between two strings (number of unequal characters) """
    return np.sum(~(np.array(list(s1)) == np.array(list(s2))))
