import re
import doctest


def get_numbers(string):
    '''
    >>> get_numbers('get_numbers takes a string and outputs a list of floating point numbers. e.g. 100.0 or 13.001, not 22')
    [100.0, 13.001, 22.0]

    >>> get_numbers('goat time')
    []

    >>> get_numbers('1e3')
    [1000.0]
    '''

    # matcher = re.compile(r'[0-9]+\.?[0-9]*')
    ematcher = re.compile(r'[0-9]+\.?[0-9]*[eE]?[0-9]*')
    # lst = matcher.findall(string)
    elst = ematcher.findall(string)
    # print(elst)
    print([float(s) for s in elst if s[0] != 'e'])
    # return [float(s) for s in lst]

if __name__ == '__main__':
    print('DOCTESTS: ' + str(doctest.testmod()))
