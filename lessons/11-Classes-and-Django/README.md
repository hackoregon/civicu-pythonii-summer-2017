# Django

1. Attendance
2. Exercisms (total of 6)
3. Django MTV
4. Modify a Model
5. Add a View
6. Add a Template
7. Add a URL
8. Admin List View with Search

## Exercisms

### Pangram


```python
def is_pangram(s):
    """Return True if str `s` is a pangram, False otherwise

    >>> is_pangram("The quick brown fox jumped over the lazy dog.')
    True
    >>> is_pangram("The slow brown fox jumped over the lazy dog.')
    False
    """
    return len(set([c for c in s.lower() if 'a' <= c <= 'z'])) == 26
```


### DNA->RNA transcription


```python
def to_rna(s):
    """Return DNA sequence of amino acid symbols transcribed to an RNA sequence

    Return empty string on any invalid DNA symbol sequence!
    >>> to_rna('GCTA')
    'CGAU'
    >>> to_rna('GCTAU')  # don't transcribe the valid chars if any are invalid
    """
    for c in s:
        if c not in 'GCTA':
            return ''
    d = defaultdict(str)
    d.update({ord('G'): 'C', ord('C'): 'G', ord('T'): 'A', ord('A'): 'U'})
    return s.translate(d)
```

### Hamming


```python
import numpy as np


def distance(s1, s2):
    """Hamming distance between two strings (number of unequal characters)

    >>> distance('ABC', 'DEF')
    3
    >>> distance('ABC', 'ABC')
    0
    """
    return np.sum(~(np.array(list(s1)) == np.array(list(s2))))
```

## Classes

A really simple class, without any constraints or "validation" of stored data.

```python

class Vehicle:
    """ A class for holding information about a Vehicle

    >>> mycar = Vehicle()
    >>> print(mycar.tag)
    AttributeError: 'Vehicle' object has no attribute 'tag'
    >>> mycar.tag = '396 FUF'
    >>> mycar.vin = 1234567890123456
    >>> mycar
    <__main__.Vehicle object at 0x7fd0dcf4b898>
    >>> mycar.__dict__
    {'tag': '396 FUF', 'vin': 1234567890123456}
    >>> type(mycar)
    __main__.Vehicle
    """
    pass
```

A slightly better class that uses class attributes to set "initial" parameters.

```python

class Vehicle:
    """ A class for holding information about a Vehicle

    >>> mycar = Vehicle()
    >>> mycar.tag = '396 FUF'
    >>> mycar.vin = 1234567890123456
    >>> mycar
    <__main__.Vehicle object at 0x7fd0dcf4b898>
    >>> mycar.__dict__
    {'tag': '396 FUF', 'vin': 1234567890123456}
    >>> type(mycar)
    __main__.Vehicle
    >>> print(mycar.make)
    AttributeError: 'Vehicle' object has no attribute 'make'
    """
    tag = ''
    vin = ''
    make = 'Tesla'
    model = ''
```

At least we can depend on it having some attributes that we need.

Now lets implement a proper constructor.

```python

class Vehicle:
    """ A class for holding information about a Vehicle

    >>> mycar = Vehicle()
    >>> mycar.tag = '396 FUF'
    >>> mycar.vin = 1234567890123456
    >>> mycar
    <__main__.Vehicle object at 0x7fd0dcf4b898>
    >>> mycar.__dict__
    {'tag': '396 FUF', 'vin': 1234567890123456}
    >>> type(mycar)
    __main__.Vehicle
    """
    def __init__(self, vin='', tag='', make='Tesla', model='', features=None):
        self.vin = vin
        self.tag = tag
        self.make = make
        self.model = model
        self.features = set(features or set())

    def is_manual(self):
        return 'manual transmission' in self.features

    def __svtr__(self):
        return repr(self)

    def __repr__(self):
        return 'Vehicle(tag={tag}, features={features})'.format(**self.__dict__)
```

What about inheritance?

```python
class SelfDrivingCar(Vehicle):
    """ A class for storing information and behaviors for Self-Driving Car objects

    >>> mycar2 = SelfDrivingCar(make='Toyota')
    >>> mycar2
    Vehicle(tag=, features=set())
    """
    autonomy_level = 1

    def __init__(self, autonomy_level=autonomy_level, **kwargs):
        super(SelfDrivingCar, self).__init__(**kwargs)

    def can_I_sleep(self):
        return self.autonomy_level > 3
```

What if I want to copy paste this init fun for a lot of other classes:


```python
class SelfDrivingCar(Vehicle):
    autonomy_level = 1

    def __init__(self.__class__, autonomy_level=autonomy_level, **kwargs):
        super(SelfDrivingCar, self).__init__(**kwargs)

    def can_I_sleep(self):
        return self.autonomy_level > 3
```

## Django

Data flow in Django

```text
Client -> HTTP request [-> nginx/apache/whitenoise] -> gunicorn -> wsgi
(Browser)                                                             |
   ^                                                                  |
   |                                                                  v
   - HTTP response <- template.html <- models.py <- views.py <- urls.py
```

Another way to think about it

```text
database.sqlite3 -> models.py -> views.py -> template.html -> urls.py -> Browser
```

### Model

Models give you (and django) a pythonic way of defining the structure (schema) of your database and then accessing your data through an ORM (Object Relational Mapping = objects that represent data records from your database).

  - query for records (QuerySet)
  - create tables
  - modify tables without losing data from the existing tables
  - add records to your database tables
  - maintaining valid relationships between your tables (query validation)

### View

You need one view for each "kind" of page you want in your app.

- Home page (list of images in our DB?)
- Image "details" page, a form for viewing, changing, or uploading an Image
- Image upload page
- A way to label an image
- Display the aggregate (sum) of the label "votes" for an image
- List the individual votes for an Image 

### Template

A template holds all the HTML "around" the data that the view will insert into the template tags. It tells the browser *"how"* to display the data. The view just says *"what"* the data is.

### URL

A URL tells the server which view to use for a particular GET request.