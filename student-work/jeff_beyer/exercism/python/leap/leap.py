'''plain
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
'''

''' 
year % 4 will be 0 for any year that IS a leap year
year % 100 will be 0 for any year that IS NOT a leap year
but year % 400 will be for any year that IS a leap year
'''
def is_leap_year(year):
    if not year % 4: # Has to be divisible by 4 at least
        if not year % 100: # But if it's divisible by 100
            if not year % 400: # it only is a leap if divisible by 400 then
                return True
            else: # Otherwise no leap year
                return False
        else: # But if it's not divisible by 100, we're good.
            return True
    else: # Not divisible by 4 = not a leap year
        return False


