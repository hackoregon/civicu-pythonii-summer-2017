from collections import defaultdict


def to_rna(s):
    """Return DNA sequence of amino acid symbols transcribed to an RNA sequence

    Return empty string on any invalid DNA symbol sequence!
    >>> to_rna('GCTA')
    'CGAU'
    >>> to_rna('GCTAU')  # don't transcribe the valid chars if any are invalid
    """
    for c in s:
        if c not in 'GCTA':
            return ''
    d = defaultdict(str)
    d.update({ord('G'): 'C', ord('C'): 'G', ord('T'): 'A', ord('A'): 'U'})
    return s.translate(d)
