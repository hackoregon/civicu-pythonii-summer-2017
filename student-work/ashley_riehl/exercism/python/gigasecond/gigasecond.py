from datetime import datetime, timedelta

def add_gigasecond(input_dt):
    return input_dt + timedelta(0,10**9)
