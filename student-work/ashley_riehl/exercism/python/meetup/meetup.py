import datetime
import re
import calendar

def meetup_day(year, month, day, week):
    c = calendar.monthcalendar(year, month)
    day, week = day.lower(), week.lower()

    #Get day index
    days_list = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
    day_num = days_list.index(day[0:2])
    print(day_num)

    #Get list of possible dates
    possible_dates = []
    for list in c:
        if list[day_num] > 0:
            possible_dates.append(list[day_num])
    print(possible_dates)

    #Determine week
    if week == "teenth":
        for date in possible_dates:
            if (date > 12) & (date < 20):
                day = date
    elif week == "last":
        day = possible_dates[-1]
    else:
        for character in week:
            try:
                week_num = int(character)
            except:
                continue
        day = possible_dates[week_num - 1]
    return datetime.date(year, month, day)
    # print(year, month, day)

# meetup_day(2013, 5, 'Monday', 'teenth')
#date(2013, 5, 13)
