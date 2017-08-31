# Review

## Documentation

How do you write a docstring for a...

- package
- module
- function
- class
- class method
- python script

- How do you write a doctest?
- How do you run doctests?
- How do you write a test for a Django app?
- How do you run tests for a Django app?
- How do you run tests for a python package?
- What do pytest unittests tests look like for a python package?
- How are they different from ordinary python unittests?
- How do you make doctests run when you test a Django app?

How do you write a unittest for:

- a Django view?
- a python script?
- a Django script?

## Debugging

- What tricks do you use to debug your python code?
- What is a Traceback?
- Where do you look first in a Traceback?
- What does a Traceback tell you?
- How can you raise an exception in python?
- How can you prevent an exception from being raised in python?

### Not on the Exam

- What does a debugger do?
- How do you set a breakpoint for a python debugger?
- How can you debug python code without using a debugger?
- How can you debug a Django app without using a debugger?

## Data Types

- dict
- Counter
- defaultdict
- list
- tuple
- namedtuple
- str
- unicode
- bytes
- set
- float
- int

## Testing

- doctest
- python unittest (pytest assert)
- Django unittest (TestCase class)

### 3 Code Challenges

Programming assignment with 10 discrete "features" (behaviors).
All of these behaviors will be present in my labeler app or the `lessons/` folder, for your use as a pattern.
There will be several ways to solve each of these 3 problems.
You can use brute force or elegant data structures.
As long as it works you'll get full credit.

The features will check your understanding of:

- loops and iterables

	while
	for

- conditionals

	if else
	not
	in
	Bool

- list comprehension

	list = [1,2,3,4,5]
	x = [x for x in list]

- coercion

	Returns a tuple consisting of the two numeric arguments converted to a common type.

	>>> coerce(1, 1.5)
	(1.0, 1.5)
	>>> coerce(1 + 2j, 1)
	((1+2j), (1+0j))
	>>> coerce(1.0, 1+3j)
	((1+0j), (1+3j))
	>>> coerce('foo', 1+3j)
	Traceback (most recent call last):
	  File "<interactive input>", line 1, in <module>
	TypeError: number coercion failed

- classes
- functions
- a CSV file
- a JSON string

	>>> import json
	>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
	'["foo", {"bar": ["baz", null, 1.0, 2]}]'

	decoding JSON

	>>> import json
	>>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
	[u'foo', {u'bar': [u'baz', None, 1.0, 2]}]


- a django View

	A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.

	from django.http import HttpResponse
	import datetime

	def current_datetime(request):
	    now = datetime.datetime.now()
	    html = "<html><body>It is now %s.</body></html>" % now
	    return HttpResponse(html)


- a command line script

	$ python -c 'import foo; print foo.hello()'

	or

	if __name__ == '__main__':
	    hello()

- `*args`

	>>> range(3,6)
	[3,4,5]
	>>> args = [3,6]
	>>> range(*args)
	[3,4,5]

- `**kwargs`

	>>> def table_things(**kwargs):
	...     for name, value in kwargs.items():
	...         print( '{0} = {1}'.format(name, value))
	...
	>>> table_things(apple = 'fruit', cabbage = 'vegetable')
	cabbage = vegetable
	apple = fruit


- `dict`s, `list`s, `tuple`s, `OrderedDict`s, `defaultdict`s


	Tuples may be constructed in a number of ways:

		Using a pair of parentheses to denote the empty tuple: ()
		Using a trailing comma for a singleton tuple: a, or (a,)
		Separating items with commas: a, b, c or (a, b, c)
		Using the tuple() built-in: tuple() or tuple(iterable)

	The constructor builds a tuple whose items are the same and in the same order as iterable’s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a tuple, it is returned unchanged. For example, tuple('abc') returns ('a', 'b', 'c') and tuple( [1, 2, 3] ) returns (1, 2, 3). If no argument is given, the constructor creates a new empty tuple, ().

	Note that it is actually the comma which makes a tuple, not the parentheses. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity. For example, f(a, b, c) is a function call with three arguments, while f((a, b, c)) is a function call with a 3-tuple as the sole argument.


	Lists may be constructed in several ways:

		Using a pair of square brackets to denote the empty list: []
		Using square brackets, separating items with commas: [a], [a, b, c]
		Using a list comprehension: [x for x in iterable]
		Using the type constructor: list() or list(iterable)

	The constructor builds a list whose items are the same and in the same order as iterable’s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a list, a copy is made and returned, similar to iterable[:]. For example, list('abc') returns ['a', 'b', 'c'] and list( (1, 2, 3) ) returns [1, 2, 3]. If no argument is given, the constructor creates a new empty list, [].


	Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

	It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

	The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

	Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order (if you want it sorted, just use sorted(d.keys()) instead). [2] To check whether a single key is in the dictionary, use the in keyword.



	A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key.

	>>> from collections import defaultdict
	>>> food_list = 'spam spam spam spam spam spam eggs spam'.split()
	>>> food_count = defaultdict(int) # default value of int is 0
	>>> for food in food_list:
	...     food_count[food] += 1 # increment element's value by 1
	...
	defaultdict(<type 'int'>, {'eggs': 1, 'spam': 7})

	An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

	A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order. In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator.

- nested data structures (dict of lists of tuple of dict ...)
- `getattr()`

	>>> class Person():
	...     name = 'Victor'
	...     def say(self, what):
	...         print(self.name, what)
	... 
	>>> getattr(Person, 'name')
	'Victor'
	>>> attr_name = 'name'
	>>> person = Person()
	>>> getattr(person, attr_name)
	'Victor'
	>>> getattr(person, 'say')('Hello')
	Victor Hello


- `.get()`

	Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

- `try/except` 
- `tuple`
- `zip`

	Make an iterator that aggregates elements from each of the iterables.

	Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

	zip() in conjunction with the * operator can be used to unzip a list:

	>>> x = [1, 2, 3]
	>>> y = [4, 5, 6]
	>>> zipped = zip(x, y)
	>>> list(zipped)
	[(1, 4), (2, 5), (3, 6)]
	>>> x2, y2 = zip(*zip(x, y))
	>>> x == list(x2) and y == list(y2)
	True

- `np.array`

	In general, numerical data arranged in an array-like structure in Python can be converted to arrays through the use of the array() function. The most obvious examples are lists and tuples. See the documentation for array() for details for its use. Some objects may support the array-protocol and allow conversion to arrays this way. A simple way to find out if the object can be converted to a numpy array using array() is simply to try it interactively and see if it works! (The Python Way).

	Examples:

	>>> x = np.array([2,3,1,0])
	>>> x = np.array([2, 3, 1, 0])
	>>> x = np.array([[1,2.0],[0,0],(1+1j,3.)]) # note mix of tuple and lists,
	    and types
	>>> x = np.array([[ 1.+0.j, 2.+0.j], [ 0.+0.j, 0.+0.j], [ 1.+1.j, 3.+0.j]])

- `pd.DataFrame`

	Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure

- GET request

	import urllib.requests
	urllib.request.urlopen("http://www.example.com/foo/bar").read()

- Django

	What is Django?

	Django (/ˈdʒæŋɡoʊ/ jang-goh) is a free and open source web application framework, written in Python. A web framework is a set of components that helps you to develop websites faster and easier.

	When you're building a website, you always need a similar set of components: a way to handle user authentication (signing up, signing in, signing out), a management panel for your website, forms, a way to upload files, etc.

	Luckily for you, other people long ago noticed that web developers face similar problems when building a new site, so they teamed up and created frameworks (Django being one of them) that give you ready-made components to use.

	Frameworks exist to save you from having to reinvent the wheel and to help alleviate some of the overhead when you’re building a new site.

	Why do you need a framework?

	To understand what Django is actually for, we need to take a closer look at the servers. The first thing is that the server needs to know that you want it to serve you a web page.

	Imagine a mailbox (port) which is monitored for incoming letters (requests). This is done by a web server. The web server reads the letter and then sends a response with a webpage. But when you want to send something, you need to have some content. And Django is something that helps you create the content.

	What happens when someone requests a website from your server?

	When a request comes to a web server, it's passed to Django which tries to figure out what is actually requested. It takes a web page address first and tries to figure out what to do. This part is done by Django's urlresolver (note that a website address is called a URL – Uniform Resource Locator – so the name urlresolver makes sense). It is not very smart – it takes a list of patterns and tries to match the URL. Django checks patterns from top to bottom and if something is matched, then Django passes the request to the associated function (which is called view).

	Imagine a mail carrier with a letter. She is walking down the street and checks each house number against the one on the letter. If it matches, she puts the letter there. This is how the urlresolver works!

	In the view function, all the interesting things are done: we can look at a database to look for some information. Maybe the user asked to change something in the data? Like a letter saying, "Please change the description of my job." The view can check if you are allowed to do that, then update the job description for you and send back a message: "Done!" Then the view generates a response and Django can send it to the user's web browser.

	Of course, the description above is a little bit simplified, but you don't need to know all the technical things yet. Having a general idea is enough.


- DRF

10 Multiple Choice Questions about fundamentals of python.
You're not allowed to Google, but you are allowed to use all the resources and code installed on your machine.
It will test all of the concepts above plus some of these below.

- `%` as a string interpolator
- float vs int
- coercion and dynamic typing

	In a dynamically typed language, every variable name is (unless it is null) bound only to an object.
	Names are bound to objects at execution time by means of assignment statements, and it is possible to bind a name to objects of different types during the execution of the program

- *args and **kwargs
- PEP8

	PEPs are Python Enhancement Proposals, and they describe and document the way python language evolves. They also provide a reference point (and a standard) for the pythonic way to write code. This is just the style guide for Python Code. 

- Django MTV architecture and how everything fits together

# Advanced

Bonus questions may cover things like

- `and`/`or` vs `&`/`|`
- `np.array` vs python `list`
- NaNs vs Nones
- `%` (mod) as a binary math operator
