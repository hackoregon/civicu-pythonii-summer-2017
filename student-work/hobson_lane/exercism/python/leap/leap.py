def is_leap_year(yr):
    """ Is the integer year (0-100000) a leap year
    return true on every year that is evenly divisible by 4
                except every year that is evenly divisible by 100
                    unless the year is also evenly divisible by 400
    """
    return bool(not yr % 4 and (yr % 100 or not yr % 400))
