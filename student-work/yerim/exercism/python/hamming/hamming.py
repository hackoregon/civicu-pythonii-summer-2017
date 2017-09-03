def distance(seq1, seq2):

    hamming_dist = 0

    if len(seq1) != len(seq2):
        raise ValueError

    for pos in range(len(seq1)):
        if seq1[pos] is not seq2[pos]:
            hamming_dist += 1

    return hamming_dist