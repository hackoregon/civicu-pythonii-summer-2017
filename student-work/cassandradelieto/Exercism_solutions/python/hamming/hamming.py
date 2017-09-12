def distance(strand1, strand2):
    hamming = 0

    #Make sure there is even an input
    if strand1 is None or strand2 is None:
        raise ValueError('None value was passed for strand.')

    #convert input value into string in case there was human error input
    if len(str(strand1)) != len(str(strand2)):
        raise ValueError('Strands not equal!')

    for x, y in zip(strand1, strand2):
        if x != y:
            hamming +=1
    return hamming


#if __name__ == '__main__':
    #print(distance("AA", "AAGGGGA"))
    #print(distance(None, "AAGGGGA"))
