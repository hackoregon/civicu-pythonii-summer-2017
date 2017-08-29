from datetime import datetime
import re

def meetup_day(year, month, day, week):
    year = year
    print("Year: {}".format(year))
    day, week = day.lower(), week.lower()
    print("Month: {}".format(month))
    print("Day: {}".format(day))
    # dow = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    #Get week number
    if week == "teenth":
        week_num = 6
    else:
        for character in week:
            try:
                week_num = int(character)
            except:
                continue

    print("Week number: {}".format(week_num))

    # datetime.date(year, month, )

meetup_day(2013, 5, 'monday', '1st')



# https://pymotw.com/2/calendar/
# import calendar
#
# # Show every month
# for month in range(1, 13):
#
#     # Compute the dates for each week that overlaps the month
#     c = calendar.monthcalendar(2007, month)
#     first_week = c[0]
#     second_week = c[1]
#     third_week = c[2]
#
#     # If there is a Thursday in the first week, the second Thursday
#     # is in the second week.  Otherwise the second Thursday must
#     # be in the third week.
#     if first_week[calendar.THURSDAY]:
#         meeting_date = second_week[calendar.THURSDAY]
#     else:
#         meeting_date = third_week[calendar.THURSDAY]
#
#     print '%3s: %2s' % (month, meeting_date)
