from datetime import timedelta, datetime

def add_gigasecond(start):
    dt = timedelta(seconds=10**9)

    return start + dt
