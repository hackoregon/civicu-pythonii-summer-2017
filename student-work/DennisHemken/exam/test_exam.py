import unittest
import exam

class TestMyAnswers(unittest.TestCase):
    
    expected_answers = ['B', 'D', 'B', 'ACF', 'AF', 'AEG', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']

    def test_question_1(self):
       self.assertEqual(exam.MY_ANSWERS[0], self.expected_answers[0])

    def test_question_2(self):
       self.assertEqual(exam.MY_ANSWERS[1], self.expected_answers[1])

    def test_question_3(self):
       self.assertEqual(exam.MY_ANSWERS[2], self.expected_answers[2])

    def test_question_4(self):
       self.assertEqual(exam.MY_ANSWERS[3], self.expected_answers[3])

    def test_question_5(self):
       self.assertEqual(exam.MY_ANSWERS[4], self.expected_answers[4])

    def test_question_6(self):
       self.assertEqual(exam.MY_ANSWERS[5], self.expected_answers[5])

    def test_question_7(self):
       self.assertEqual(exam.MY_ANSWERS[6], self.expected_answers[6])

    def test_question_8(self):
       self.assertEqual(exam.MY_ANSWERS[7], self.expected_answers[7])

    def test_question_9(self):
       self.assertEqual(exam.MY_ANSWERS[8], self.expected_answers[8])

    def test_question_10(self):
       self.assertEqual(exam.MY_ANSWERS[9], self.expected_answers[9])                        

    def test_question_11(self):
       self.assertEqual(exam.MY_ANSWERS[10], self.expected_answers[10])


if __name__ == '__main__':
    unittest.main()

