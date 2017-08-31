## Exercisms

### Pangram


```python
def is_pangram(s):
    """Return True if str `s` is a pangram, False otherwise

    >>> is_pangram("The quick brown fox jumped over the lazy dog.')
    True
    >>> is_pangram("The slow brown fox jumped over the lazy dog.')
    False
    """
    return len(set([c for c in s.lower() if 'a' <= c <= 'z'])) == 26
```


### DNA->RNA transcription


```python
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
```

### Hamming


```python
import numpy as np


def distance(s1, s2):
    """Hamming distance between two strings (number of unequal characters)

    >>> distance('ABC', 'DEF')
    3
    >>> distance('ABC', 'ABC')
    0
    """
    return np.sum(~(np.array(list(s1)) == np.array(list(s2))))
```


