import re


def find_numbers(string):
    matcher = re.compile(r'[0-9]+[.eE]?[0-9]?')
    nums = matcher.findall(string)
    # return nums
    print(nums)
    return [float(num) for num in nums]


print(find_numbers('Create a regular expression that can find all the ' +
      'floating point de347cimal numbers 50 in a string, like $1000.00 or 1e3 ' +
      'or 1000.0001.')) 

print(find_numbers('1000'))