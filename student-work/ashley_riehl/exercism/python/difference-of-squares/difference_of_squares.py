def square_of_sum(num):
    return sum(list(range(num + 1))) ** 2

def sum_of_squares(num):
    sum_total = 0
    for each in range(num + 1):
        sum_total += (each ** 2)
    return sum_total

def difference(num):
    return square_of_sum(num) - sum_of_squares(num)
