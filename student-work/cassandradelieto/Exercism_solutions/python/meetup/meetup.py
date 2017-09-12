from datetime import date, timedelta
from calendar import day_name, isleap


def meetup_day(year, month, weekday, descriptor):
    '''Given examples of a meetup dates, each containing a month, day, year, and descriptor
    (first, second, teenth, etc), calculate the date of the actual meetup.
    For example, if given "First Monday of January 2017", the correct meetup date is 2017/1/2
    expressed as date(YYYY,MM,DD)
    '''

    DESCRIPTORS = {
        '1st': 1,
        '2nd': 8,
        '3rd': 15,
        '4th': 22,
        '5th': 29,
        'teenth': 13,
                   }

    start = date(year, month, DESCRIPTORS.get(descriptor, last(year, month))) #.get(key, default)
    offset = list(day_name).index(weekday) - start.weekday()
    return start + timedelta(days = offset % 7)

def last(year, month):
    return([25,22 + int(isleap(year))] + [25,24,25,24,25]*2)[month-1]


#list(calendar.day_name) = list of all day names
#days.index(day) = get the index of the selected day
