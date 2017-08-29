def is_isogram(phrase):
    phrase = phrase.replace(' ', '').replace('-', '').lower()
    split = [letter for letter in phrase]
    split_set = {letter for letter in split}

    if len(split) == len(split_set):
        return True
    else:
        return False

is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax")
