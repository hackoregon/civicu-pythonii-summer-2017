import calendar
from datetime import date

def meetup_day(yr, month, day, string):
    curr_month = calendar.monthcalendar(yr, month)

    if day is 'Monday':
        day = 0
    elif day is 'Tuesday':
        day = 1
    elif day is 'Wednesday':
        day = 2
    elif day is 'Thursday':
        day = 3
    elif day is 'Friday':
        day = 4
    elif day is 'Saturday':
        day = 5
    elif day is 'Sunday':
        day = 6


    if string[0].isdigit():
        condition = int(string[0]) - 1
        first = curr_month[0][day]
        if first is not 0:
            calc_date = curr_month[condition][day]
            return date(yr, month, calc_date)
        else:
            calc_date = curr_month[condition + 1][day]
            return date(yr, month, calc_date)

    elif string is 'teenth':
        start = 1
        calc_date = curr_month[start][day]
        while calc_date < 13:
            start += 1
            calc_date = curr_month[start][day]
        else:
            return date(yr, month, calc_date)

    elif string is 'last':
        if curr_month[-1][day] is not 0:
            calc_date = curr_month[-1][day]
            return date(yr, month, calc_date)
        else:
            calc_date = curr_month[-2][day]
            return date(yr, month, calc_date)


