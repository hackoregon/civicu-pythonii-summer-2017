import unittest

from regexp_practice import number_finder


class RegExTeste(unittest.TestCase):
    def test_dollarsign(self):
        self.assertEqual(number_finder('like $1000.00'), [1000.0])
    def test_e(self):
        self.assertEqual(number_finder('or 1e3'), [1000.0])
    def test_list(self):
        self.assertEqual(number_finder('like $1000.00 or 1e3 or 1000.0001'), [1000.0, 1000.0, 1000.0001])

if __name__ == '__main__':
    unittest.main()
