import unittest

from regex_practice import find_numbers


class RegexTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(find_numbers('Create a regular expression that can find all the floating point decimal numbers in a string, like $1000.00 or 1e3 or 1000.0001.'), [1000.0, 1000.0, 1000.0001])


if __name__ == '__main__':
    unittest.main()