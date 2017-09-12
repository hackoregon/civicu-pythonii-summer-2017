import unittest
import exam
import json


class TestExam(unittest.TestCase):

    def test_questions(self):
        self.assertEqual(exam.QUESTIONS, [str(i) for i in range(11)])

    def test_questions_length(self):
        self.assertEqual(len(exam.QUESTIONS), 11)

    def test_question_texts(self):
        self.assertEqual(exam.QUESTION_TEXTS, ['What python builtin type (comes with python in the standard library) is best for counting the number of occurences of values in a sequence or array.', 'What mutable python data type stores a mapping between keys and values, allows you to add new keys, and ensures that all keys are unique.', 'What python builtin function can be used to create a `list` of of 3-`tuple`s (triplets) out of 3 `list`s of objects.', 'Which of the following help resources are only available in ipython/jupyter console or notebook (and are **not** available in a plain python interpreter or console)', 'Which of the following data types were changed significantly in python3.5 relative to python 2.7', 'Which of the following operators can be used as unary operators in python', 'Which of the following operators can be used as binary operators in python', 'What method can be used to retrieve all the variable names in your global context as strings', 'What builtin function could you use to assemble paths from a list of directories in python for cross-platform compatibility', 'What python builtin function can be used to sort a list of 2-tuples.', 'Which of the following are pythonic (part of `this` Zen of Python)'])

    def test_question_texts_length(self):
        self.assertEqual(len(exam.QUESTION_TEXTS), 11)

    def test_answers(self): # actually contains INCORRECT answers because that's what it says on GitHub initially
        self.assertEqual(exam.ANSWERS, ['defaultdict', 'values_count', '.distinct()', '.count_values()', 'len', 'dict', 'set', 'list', 'enum', 'namedtuple', 'tuple', 'zip', 'dict', 'list', 'set', 'zip', 'iter', 'vars', 'vars()', 'dir()', 'help()', '.__doc__', 'int', 'float', 'tuple', 'list', 'bool', 'and', 'or', '/', '%', 'not', 'keys()', 'locals().keys()', 'str()', 'list()', 'help()', '', "'/’.split()", "'/’.join()", 'dirs', 'os.dup', 'os.build', 'sortdict', 'sort', 'order', 'ordered', 'list', 'dict'])

    def test_answers_length(self):
        self.assertEqual(len(exam.ANSWERS), 49)

    def test_my_answers(self):
        self.assertEqual(exam.MY_ANSWERS, ['B', 'D', 'BE', 'ACF', 'AF', 'AEG', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG'])

    def test_json_is_correct_format(self):
        self.assertTrue(json.loads(exam.MY_ANSWERS_JS))


if __name__ == '__main__':
    unittest.main()
