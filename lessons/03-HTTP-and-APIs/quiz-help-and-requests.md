# Quiz Questions

Q: Name at least 3 ways to get help about a function, class or object

A: `help` to display docstring
```python
>>> import requests
>>> help(requests.get)
get(url, params=None, **kwargs)
    Sends a GET request.
    
    :param url: URL for the new :class:`Request` object.
...
```

A: `?` to display docstring
```python
>>> import csv
>>> csv?
Type:        module
String form: <module 'csv' from '/usr/lib/python3.5/csv.py'>
File:        /usr/lib/python3.5/csv.py
Docstring:  
CSV parsing and writing.

This module provides classes that assist in the reading and writing
of Comma Separated Value (CSV) files, and implements the interface
...
```

A: `??` to display source code (as well as the docstring)
```python
>>> import requests
>>> requests.get??
Signature: requests.get(url, params=None, **kwargs)
Source:   
def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)

...
```

A: These work in python as well as ipython:
```python
>>> print(function.__doc__)
>>> dir(object_instance)
>>> vars(object_instance)
>>> import json  # just to make dictionaries look nicer when printed
>>> print(json.dumps(object_instance.__dict__, indent=2))
```

* What is a linter?
* Name a popular linter for python.
* What is PEP8?
* What's the difference between a `str` object and a `bytes` object?
* What kind of strings have a `decode()` method?
* What kind of strings have an `encode()` method?
* What kind of encoding is the default for all unicode strings in python?
* What kind of encoding does Microsoft often use for CSV files and other text files (including database dumps)?
* What are some clues for when you should probably modularize your code?
* What is Pandas?
* What is Django
* What is MVC?
* What is MVT or MTV?
* What is an API?
* What is the first character in the url after the path and before the first parameter or argument in an API reqwuest?
* How do you convert unicode into bytes?
* How do you convert bytes into unicode?
* What is the "separator" between parameters (arguments) in an API query (GET request)?
* What is an API endpoint?
* How can you access the shell from the inside of ipython?
* Package manager to install `pip` on Mac?
* Package manager to install `pip` on Win?
* Package manager to install `pip` on Lin?
* Package manager to install python packages?
* What type of object is `u"Hello_world"`
* What type of object is `b"Hello_world"`
* What type of object is `r"Hello_world"`
* What is a good style guide for python?
* Where can you find the definition of pythonic code?


