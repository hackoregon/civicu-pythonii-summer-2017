def to_rna(dna):
    dna = dna.lower()
    dna = ''.join(filter(str.isalpha, dna))

    rna = ''

    for nucleotide in dna:
        if nucleotide is 'a':
            rna = rna + 'U'
        elif nucleotide is 't':
            rna = rna + 'A'
        elif nucleotide is 'g':
            rna = rna + 'C'
        elif nucleotide is 'c':
            rna = rna + 'G'
        else:
            rna = ''
            break

    return rna
