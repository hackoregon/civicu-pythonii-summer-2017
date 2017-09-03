import datetime
from calendar import Calendar

def meetup_day(year, month, day, occurance):
    year = year
    month = month
    if day == 'Monday':
        day_ind = 0
    elif day == 'Tuesday':
        day_ind = 1
    elif day == 'Wednesday':
        day_ind = 2
    elif day == 'Thursday':
        day_ind = 3
    elif day == 'Friday':
        day_ind = 4
    elif day == 'Saturday':
        day_ind = 5
    elif day == 'Sunday':
        day_ind = 6

    possible_days = list()
    for d in Calendar().itermonthdays(year, month):
        try:
            if datetime.datetime(year, month, d).weekday() == day_ind:
                possible_days.append(d)
        except ValueError:
            continue

    if occurance == '1st':
        select_ind = 0
    elif occurance == '2nd':
        select_ind = 1
    elif occurance == '3rd':
        select_ind = 2
    elif occurance == '4th':
        select_ind = 3
    elif occurance == '5th':
        select_ind = 4
    elif occurance == 'last':
        select_ind = -1
    elif occurance == 'teenth':
        for pday in possible_days:
            if pday in [13, 14, 15, 16, 17, 18, 19]:
                try:
                    ret_date = datetime.date(year, month, pday)
                except:
                    raise MeetupDayException
                
                return ret_date
    try:
        ret_date = datetime.date(year, month, possible_days[select_ind])
    except:
        raise MeetupDayException

    return ret_date
