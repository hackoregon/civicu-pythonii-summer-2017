def decode(string):
    # Init the output string (in this case, decoded)
    new_string = ''

    # If there's nothing input, return the empty string
    if not string:
        return new_string

    # Letter index counter
    letter_ind = 0

    # Looping over the string, letter by letter
    while True:
        # Ensure we don't index past the length
        try:
            this_letter = string[letter_ind]
        except IndexError:
            # If we do, return our string.
            return new_string
        # Carry through a space
        if this_letter == ' ':
            new_string += ' '
            letter_ind += 1
            continue
        # If this letter is a digit (number)
        if this_letter.isdigit():
            # If the next is not a digit
            if not string[letter_ind+1].isdigit():
                # Add this digit number repeats
                string_add = int(this_letter) * string[letter_ind+1]
                # Skip ahead correctly
                letter_ind += 2
            # This handles 2 (but not 3!) digit numbers
            else:
                string_add = (int(string[letter_ind:letter_ind+2]) *
                              string[letter_ind+2])
                letter_ind += 3
            # Add to our new string
            new_string += string_add
            continue
        # If it's just a letter, add it and move on
        else:
            new_string += this_letter
            letter_ind += 1


def encode(string):
    # Init the output string (in this case, encoded)
    new_string = ''

    # If there's nothing input, return the empty string
    if not string:
        return new_string

    # Letter index counter
    letter_ind = 0

    # Looping over the string, letter by letter
    while True:
        # Ensure we don't index past the length
        try:
            this_letter = string[letter_ind]
        except IndexError:
            # If we do, return our string.
            return new_string

        # Initialize the count for each letter
        letter_count = 1
        while True:
            # Nested loop, to look past the start index and see how many
            # repititions we may have
            letter_ind += 1
            # Protects us from over indexing
            try:
                next_letter = string[letter_ind]
            except IndexError:
                # As an exit, if we only have one count, just add the letter
                if letter_count == 1:
                    new_string += this_letter
                # But if we have more than one count, add the num and letter
                else:
                    new_string += str(letter_count) + this_letter
                break
            # Increment our count if the letters match
            if this_letter == next_letter:
                letter_count += 1
            else:
                # Same exit criteria as IndexError
                if letter_count == 1:
                    new_string += this_letter
                else:
                    new_string += str(letter_count) + this_letter
                break
