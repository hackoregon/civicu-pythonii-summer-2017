# Pangram
'''
Determine if a sentence is a pangram. A pangram is a sentence using every letter
 of the alphabet at least once.
The best known English pangram is: 
> The quick brown fox jumps over the lazy dog.

The alphabet used consists of ASCII letters `a` to `z`, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
'''
def is_pangram(string):
    for letter in range(ord('a'),ord('z')):
        if chr(letter) not in string.lower():
            # If any letter isn't in there, we bounce.
            return False
    # If we made it here, we're good
    return True
