import unittest

import read_exam

# MY_ANSWERS = ['B', 'D', 'B', 'ACF', 'AF', 'AGE', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']

class CheckExamAnswers(unittest.TestCase):
    def question1(self):
        self.assertEqual(read_exam.MY_ANSWERS[0], 'B')

    def question2(self):
        self.assertEqual(read_exam.MY_ANSWERS[1], 'D')

    def question3(self):
        self.assertEqual(read_exam.MY_ANSWERS[2], 'B')

    def question4(self):
        self.assertEqual(read_exam.MY_ANSWERS[3], 'ACF')

    def question5(self):
        self.assertEqual(read_exam.MY_ANSWERS[4], 'AF')

    def question6(self):
        self.assertEqual(read_exam.MY_ANSWERS[5], 'AGE')

    def question7(self):
        self.assertEqual(read_exam.MY_ANSWERS[6], 'ABCDEF')

    def question8(self):
        self.assertEqual(read_exam.MY_ANSWERS[7], 'B')

    def question9(self):
        self.assertEqual(read_exam.MY_ANSWERS[8], 'CD')

    def question10(self):
        self.assertEqual(read_exam.MY_ANSWERS[9], 'B')

    def question11(self):
        self.assertEqual(read_exam.MY_ANSWERS[10], 'ABCDEFG')


if __name__ == '__main__':
    unittest.main()