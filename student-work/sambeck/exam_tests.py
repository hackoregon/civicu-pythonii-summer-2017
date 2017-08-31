import unittest
import exam


class test_load_pickle(unittest.TestCase):
    QUESTIONS, QUESTION_TEXTS, ANSWERS,\
        MY_ANSWERS, MY_ANSWERS_JS = exam.load_all()
    assert(len(QUESTIONS) == 11)
    assert(len(QUESTION_TEXTS) == 11)
    assert(len(ANSWERS) == 11)
    assert(len(MY_ANSWERS) == 11)
    assert(isinstance(MY_ANSWERS_JS, str))
