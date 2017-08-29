def is_leap_year(year):
    year_div_four = year%4
    year_div_100 = year%100
    year_div_400 = year%400
    leap_year = False
    if year_div_four == 0:
        leap_year = True
    if year_div_100 == 0: 
        if year_div_400 == 0:
            leap_year = True
        else:
            leap_year = False

    return leap_year

 