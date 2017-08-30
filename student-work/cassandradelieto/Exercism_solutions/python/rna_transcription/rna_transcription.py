def to_rna(strand):
    translation = {'G':'C', 'C':'G', 'A':'T', 'T':'A'}
    RNA = []

    for letter in strand:
        if letter in translation:
            RNA.append(translation[letter])
        else:
            return ""
#row = [RNA.append(translation[letter]) for letter in strand if letter in translation]
    return ''.join(RNA)
