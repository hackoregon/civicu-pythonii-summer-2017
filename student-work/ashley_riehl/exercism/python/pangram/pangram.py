import string

def is_pangram(input):
    input = input.strip().lower().replace(' ', '').replace('.!', '')
    input = list(input)
    input = sorted(list(set(input)))

    letters = list(string.ascii_lowercase)

    input_list = []

    for each in input:
        if each in letters:
            input_list.append(each)

    if input_list == letters:
        return True
    else:
        return False

is_pangram("Something here and there.")
