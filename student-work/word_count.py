from collections import Counter


def word_count(text):
    def replace_non_alpha(char):
        return char.lower() if char.isalnum() else ' '
    text = ''.join(replace_non_alpha(c) for c in text)
    return Counter(text.split())
