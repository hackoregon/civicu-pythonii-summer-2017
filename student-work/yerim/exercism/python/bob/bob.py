import re

def hey(input):
    input = ''.join(re.findall('[^0-9@#$%^&*() \n\r\t]', input))
    question = re.findall('\?$', input)
    capital = re.findall('[A-Z]', input)
    all_alphabet = re.findall('[a-zA-Z]', input)
    if len(input) == 0:
        return 'Fine. Be that way!'
    elif all_alphabet and len(capital) > len(all_alphabet)-1:
        return 'Whoa, chill out!'
    elif question:
        return 'Sure.'
    else:
        return 'Whatever.'