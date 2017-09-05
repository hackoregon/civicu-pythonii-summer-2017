# Bob
'''
Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question.

He answers 'Whoa, chill out!' if you yell at him.

He says 'Fine. Be that way!' if you address him without actually saying
anything.

He answers 'Whatever.' to anything else.
'''
def hey(quest):
    quest = quest.strip()
    if not quest:
        return 'Fine. Be that way!'
    if quest.isupper():
        return 'Whoa, chill out!'
    elif quest.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
    
