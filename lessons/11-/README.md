# Django

1. Attendance
2. Exercisms (total of 6)
3. Django MTV
4. Modify a Model
5. Add a View
6. Add a Template
7. Add a URL
8. Admin List View with Search

## Exercisms

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