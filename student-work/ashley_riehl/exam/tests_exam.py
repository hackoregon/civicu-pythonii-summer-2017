# Create a file called test_exam.py and write a "unittest" that checks that each of the answers
# in your answer exam.MY_ANSWERS are what you intended.

import unittest
import doctest

from exam import MY_ANSWERS, read_exam
import exam

class TestAnswers(unittest.TestCase):
    def test_first_question(self):
        self.assertEqual(MY_ANSWERS[0], "B")
    def test_last_question(self):
        self.assertEqual(MY_ANSWERS[-1], "ABCDEFG")
    def test_all_correct(self):
        self.assertEqual(MY_ANSWERS, ["B","D","B","ACF","AF","AEG","ABCDEF","B","CD","B","ABCDEFG"])
    def test_read_function_output(self):
        self.assertEqual(len(read_exam()),11)
    def test_docs(self):
        results = doctest.testmod(exam)
        self.assertEqual(results.failed, 0)

if __name__ == '__main__':
    unittest.main()
