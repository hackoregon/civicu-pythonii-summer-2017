#'Sure.' if you ask him a question.
#'Whoa, chill out!' if you yell at him.
#'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.

def hey(what):
    what = what.strip()
    if not what:
        return 'Fine. Be that way!'
    elif what.isupper():
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    else:
        return "Whatever."


hey("sup?")
hey("stop!")
hey("")
hey("Life is good")
