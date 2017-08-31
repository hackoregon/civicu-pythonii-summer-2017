def is_isogram(s):
    """ Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter.

    Examples of isograms:

    - lumberjacks
    - background
    - downstream
    """
    from collections import Counter
    s = s.lower().strip()
    s = [c for c in s if c.isalpha()]
    counts = Counter(s).values()
    return max(counts or [1]) == 1
