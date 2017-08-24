def is_leap_year(year):
    # if divisible by 4, then return true
    # if divisible by 100, then return false but if divisible by 400 then true
    if not year % 400:
        return True
    elif not year % 100:
        return False
    elif not year % 4:
        return True
