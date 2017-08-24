# Classes

## Simplest Possible Class

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

## Class Attributes for Defaults

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

## Constructor

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

Your mission is to write a `def __repr__()` that is general, so it can be pasted into any class and display *all* the attributes of that class.

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

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return '{name}({args}))'.format(
            name=type(self).__name__,
            args=', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()]))
```

## Inheritance

What about inheritance?

```python
class SelfDrivingCar(Vehicle):
    """ A class for storing information and behaviors for Self-Driving Car objects

    >>> mycar2 = SelfDrivingCar(make='Toyota')
    >>> mycar2
    Vehicle(tag=, features=set())
    """
    def __init__(self, autonomy_level=1, **kwargs):
        self.autonomy_level = autonomy_level
        super(globals()[type(self).__name__], self).__init__(**kwargs)

    def can_I_sleep(self):
        return self.autonomy_level > 3
```

What if I want to copy paste this init fun for a lot of other classes? Could we generalize it like we did for repr?


```python
class SelfDrivingCar(Vehicle):
    autonomy_level = 1

    def __init__(self.__class__, autonomy_level=autonomy_level, **kwargs):
        super(SelfDrivingCar, self).__init__(**kwargs)

    def can_I_sleep(self):
        return self.autonomy_level > 3
```