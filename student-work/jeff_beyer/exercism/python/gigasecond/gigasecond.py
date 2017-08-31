from datetime import datetime
from datetime import timedelta
'''
Calculate the moment when someone has lived for 10^9 seconds.

A gigasecond is 10^9 (1,000,000,000) seconds.
'''
def add_gigasecond(datetime_in):
    return datetime_in + timedelta(seconds=10**9)
    pass
