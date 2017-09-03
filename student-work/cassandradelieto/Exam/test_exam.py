import unittest
import doctest
import exam

from exam import read_exam, QUESTIONS, MY_ANSWERS, MY_ANSWERS_JSON

class TestExam(unittest.TestCase):

    def test_1(self):
        self.assertEqual(MY_ANSWERS[0],"B")

    def test_2(self):
        self.assertEqual(MY_ANSWERS[1],"D")

    def test_3(self):
        self.assertEqual(MY_ANSWERS[2],"B")

    def test_11(self):
        self.assertEqual(MY_ANSWERS[10],"ABCDEFG")

    def test_length_is_11(self):
        self.assertEqual(len(MY_ANSWERS), 11)

if __name__ == '__main__':
    unittest.main(exit=False) #exit=True is default and will end here.
    doctest.testmod(exam) # run: python -m doctest -v exam.py




