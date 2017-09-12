import string


def rotate(given, n):
    n = n % 26
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    mapping = dict(zip(low + up, low[n:] + low[:n] + up[n:] + up[:n]))
    #Map two lists into a dictionary
    return ''.join(mapping[ch] if ch in mapping else ch for ch in given)
#[n:] from position n
#[:n] till position n
#s[:i] + s[i:] is == s
#n[-2:] second to last, included the end.
