def square_of_sum(numbers):
    next = 0
    sum_num = 0
    for i in range(numbers):
        next += 1
        sum_num += next
    return sum_num ** 2


def sum_of_squares(numbers):
    next = 0
    sum_num = 0
    for i in range(numbers):
        next += 1
        sum_num += next ** 2
    return sum_num


def difference(numbers):
    sq_sum = square_of_sum(numbers)
    sum_sq = sum_of_squares(numbers)
    return abs(sq_sum-sum_sq)
