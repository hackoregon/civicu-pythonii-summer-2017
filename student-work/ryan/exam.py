import csv
import pandas as pd
import json
"""
    function should take csv, return three lists.
    Q's , ANSWERS, list of list mapping together questions with

    Here is my Doctest.

    >>> read_exam()
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['What python builtin type (comes with python in the standard library) is best for counting the number of occurences of values in a sequ
ence or array.', 'What mutable python data type stores a mapping between keys and values, allows you to add new keys, and ensures that all keys are unique.', 'What python bu
iltin function can be used to create a `list` of of 3-`tuple`s (triplets) out of 3 `list`s of objects.', 'Which of the following help resources are only available in ipython
/jupyter console or notebook (and are **not** available in a plain python interpreter or console)', 'Which of the following data types were changed significantly in python3.
5 relative to python 2.7', 'Which of the following operators can be used as unary operators in python', 'Which of the following operators can be used as binary operators in
python', 'What method can be used to retrieve all the variable names in your global context as strings', 'What builtin function could you use to assemble paths from a list o
f directories in python for cross-platform compatibility', 'What python builtin function can be used to sort a list of 2-tuples.', 'Which of the following are pythonic (part
 of `this` Zen of Python)'], ['B', 'D', 'B', 'ACF', 'AF', 'AGE', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG'])

"""

QUESTIONS = []
QUESTION_TEXTS = []
ANSWERS = []
MY_ANSWERS = ['B','D','B','ACF','AF', 'AGE', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']
MY_ANSWER_JS = []
SUBMISSIONS = []


def read_exam(path='/home/ryan/test/exam.csv'):
    dataf = pd.read_csv(path, header=0)
    QUESTIONS = list(dataf['question number'])
    ANSWERS = list(dataf['answer'])
    QUESTION_TEXTS = list(dataf['question'])
    print(QUESTIONS)
    print(ANSWERS)
    print(QUESTION_TEXTS)
    dictionary = dict(zip(QUESTIONS, ANSWERS))

    MY_ANSWER_JS = [{'id':key,"my_answer":value} for key,value in dictionary.items()]

    global MY_ANSWER_JS

print(read_exam())
