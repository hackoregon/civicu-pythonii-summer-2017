def detect_anagrams(anagram, word_list):
    if anagram is int and word_list is int:
        raise ValueError("No numbers allowed in comparison. Characters only")
    letters = sorted(anagram.lower()) #sort alphabetically and lower em all
    return [word for word in word_list if sorted(word.lower()) == letters and word.lower() != anagram.lower()]

