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
        return 'automatic transmission' in self.features

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'Vehicle(tag={tag}, vin={vin}, features={features})'.format(**self.__dict__)
        #Come back and fix this:
        # type(self).__name__
        # ', '.join(["{}={}".format for k, v in self.__dict__.items])
