# Regular Expressions

Let's use a regular expression to find a greeting, similar to in the bob.py exercism.

```python
>>> import re
>>> matcher = re.compile(r'Hello')
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
[]
```

That missed "hello" and "Hi" so let's make it more flexible using a binary OR (`|`) operator.

```python
>>> matcher = re.compile(r'Hello|hello')
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
['hello']
```

We're still missing "Hi".
How would you fix that?

```python
>>> matcher = re.compile(r'Hi|hi|Hello|hello')
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
['Hi', 'hello', 'hi']
```


And now use character classes to do the same thing.

```python
>>> matcher = re.compile(r'[Hh]i|ello')
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
['Hi', 'ello', 'hi']
```

That's not quite what we wanted.
We need to use parenthesis to create groups for each sequence that we want to use the OR (`|`) operator on.

```python
>>> matcher = re.compile(r'[Hh](i|ello)')
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
['i', 'ello', 'i']
```

Oops, that's worse.
When we create a group, that's the only thing that the regular expression thinks we're interested in when we do a `findall`.
So lets create 2 groups, one for the entire greeting word and one for the part after the "H"


```python
... matcher = re.compile(r'([Hh](i|ello))')
...
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
[('Hi', 'i'), ('hello', 'ello'), ('hi', 'i')]
```

Here's that expression again with a repetition count range to give you some ideas:


```python
... matcher = re.compile(r'([Hh](i|ello))')
...
>>> matcher.findall('Hi John, did you just say "hello Google" or something?')
[('Hi', 'i'), ('hello', 'ello'), ('hi', 'i')]
```

## In-Class Exercise

Create a regular expression that can find all the floating point decimal numbers in a string, like $1000.00 or 1e3 or 1000.0001.
Then coerce each of those number `str`s into `float`s (so the dollar sign shouldn't be in your number string).
Write a unittest or doctest that checks 3 numbers in one string.
If that's got you stumped, start with recognizing an integer, then work your way up.

Here's an example doctest that should pass:

```python
def find_numbers(s):
""" Finds all floating point values within a string and returns a list of those strings coerced into floats

>>> find_numbers('Create a regular expression that can find all the floating point decimal numbers in a string, like $1000.00 or 1e3 or 1000.0001')
[1000.0, 1000.0, 1000.0001]
"""

