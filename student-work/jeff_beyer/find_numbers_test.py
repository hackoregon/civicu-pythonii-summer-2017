import unittest

import find_numbers


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class find_numbers_tests(unittest.TestCase):
    def test_find_numbers(self):
        self.assertEqual(
            find_numbers.find_numbers('Create a regular expression that can ' +
                                      'find all the floating point decimal ' +
                                      'numbers in a string, like $1000.00 or' +
                                      ' 1e3 or 1000.0001.'), [1000.0, 1000.0,
                                                              1000.0001])


if __name__ == '__main__':
    unittest.main()
