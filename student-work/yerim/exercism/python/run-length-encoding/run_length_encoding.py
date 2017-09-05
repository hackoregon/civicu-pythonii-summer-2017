
def decode(string):
    output = ''
    hold = ''
    for element in string:
        if element.isalpha() or element is ' ':
            if hold:
                output = '{}{}'.format(output, element * int(hold))
                hold = ''
            else:
                output = '{}{}'.format(output, element)
                hold = ''
        else:
            hold += element
    return output


def encode(string):
    if string is '':
        return ''

    output = ''
    previous = string[0]
    count = 1
    for idx in range(1, len(string)):
        element = string[idx]
        if idx < len(string) - 1:
            if previous is element:
                count += 1
            elif count is 1:
                output = '{}{}'.format(output, previous)
                previous = element
            else:
                output = '{}{}{}'.format(output, count, previous)
                count = 1
                previous = element
        else:
            if previous is element:
                count += 1
                output = '{}{}{}'.format(output, count, previous)
            elif count is 1:
                output = '{}{}{}'.format(output, previous, element)
            else:
                output = '{}{}{}{}'.format(output, count, previous, element)

    return output
