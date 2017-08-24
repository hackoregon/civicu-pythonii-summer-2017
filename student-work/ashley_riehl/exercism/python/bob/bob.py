def hey(statement=None):
    statement = statement.strip()

    if statement.isupper():
        return 'Whoa, chill out!'
    elif statement.endswith('!') and statement.isupper():
        return 'Whoa, chill out!'
    elif statement.endswith('?'):
        return 'Sure.'
    elif len(statement) < 1:
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
