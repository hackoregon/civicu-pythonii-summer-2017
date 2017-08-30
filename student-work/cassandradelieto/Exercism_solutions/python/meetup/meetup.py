from datetime import date, timedelta
from calendar import day_name, isleap


def meetup_day(year, month, weekday, descriptor):
    '''Given examples of a meetup dates, each containing a month, day, year, and descriptor
    (first, second, teenth, etc), calculate the date of the actual meetup.
    For example, if given "First Monday of January 2017", the correct meetup date is 2017/1/2
    expressed as date(YYYY,MM,DD)
    '''
    DESCRIPTORS = {
                   1: "1st",
                   2: "2nd",
                   3: "3rd",
                   4: "4th",
                   5: "5th",
                   teenth: "teenth",
                   last: "last",
                   }

    start = date(year, month, day)
    day =
    offset = list(day_name).index(day) - start.weekday()
    return start +


#list(calendar.day_name) = list of all day names
#days.index(day) = get the index of the selected day

