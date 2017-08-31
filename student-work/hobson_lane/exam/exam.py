""" Example implementation of exam.py for the exam

>>> MY_ANSWERS_JS
[
  {
    "my_answer": "B",
    "id": 0
  },
  {
    "my_answer": "D",
    "id": 1
  },
  {
    "my_answer": "B",
    "id": 2
  },
  {
    "my_answer": "ACF",
    "id": 3
  },
  {
    "my_answer": "AF",
    "id": 4
  },
  {
    "my_answer": "AGE",
    "id": 5
  },
  {
    "my_answer": "ABCDEF",
    "id": 6
  },
  {
    "my_answer": "B",
    "id": 7
  },
  {
    "my_answer": "CD",
    "id": 8
  },
  {
    "my_answer": "B",
    "id": 9
  },
  {
    "my_answer": "ABCDEFG",
    "id": 10
  }
]
"""

import json

import pandas as pd


def read_exam(csv_path='../shared-resources/exam.csv'):
    df = pd.read_csv(csv_path, header=0)
    return (list(df['question number']), list(df['question']), list(df['answer']))


QUESTIONS, QUESTION_TEXTS, ANSWERS = read_exam()

MY_ANSWERS = list(pd.read_csv(
    'https://raw.githubusercontent.com/hackoregon/civicu-pythonii-summer-2017/ceasar/lessons/shared-resources/exam.csv',
    header=0).answer)

MY_ANSWERS_JS = json.dumps([{'id': i, 'my_answer': a} for (i, a) in enumerate(MY_ANSWERS)], indent=2)
