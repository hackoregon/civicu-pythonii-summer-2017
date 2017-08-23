def is_pangram(s):
    """Return True if str `s` is a pangram, False otherwise

    >>> is_pangram("The quick brown fox jumped over the lazy dog.')
    True
    >>> is_pangram("The slow brown fox jumped over the lazy dog.')
    False
    """
    return len(set([c for c in s.lower() if 'a' <= c <= 'z'])) == 26
