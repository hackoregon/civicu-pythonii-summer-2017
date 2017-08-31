import unittest
from exam import ANSWERS, MY_ANSWERS

class ExamTest(unittest.TestCase):

	def test_id(self):
		self.assertEqual(MY_ANSWERS, ANSWERS)


if __name__ == '__main__':
	unittest.main()