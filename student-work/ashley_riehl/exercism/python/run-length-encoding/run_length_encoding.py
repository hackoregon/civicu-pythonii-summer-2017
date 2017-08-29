def decode(input_value):
    letter = None
    final =[]
    number = 1
    for i, each in enumerate(input_value):
        try:
            number = int(each)
            try:
                number2 = int(input_value[i-1])
                number = number2 * 10 + number
            except: continue
        except:
            letter = each
            string_val = ''.join([letter for s in range(number)])
            final.append(string_val)
            number = 1
    return ''.join(final)

def encode(input_val):
    if len(input_val) > 0:
        count = 1
        encoded = []
        last_letter = None
        for letter in input_val:
            if last_letter == None:
                last_letter = letter
            elif letter == last_letter:
                count += 1
            else:
                encoded.append([str(count), last_letter])
                last_letter = letter
                count = 1
        encoded.append([str(count), last_letter])

        answer = []
        for pair in encoded:
            if pair[0] == '1':
                del pair[0]
            str_pair = ''.join(pair)
            answer.append(str_pair)
        return ''.join(answer)
    else:
        return ''
