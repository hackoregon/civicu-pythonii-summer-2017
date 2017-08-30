from datetime import timedelta

def add_gigasecond(born_date):
    gigasecond = 10**9
    return born_date + timedelta(seconds=gigasecond)

