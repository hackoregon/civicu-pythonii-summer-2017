import os
import csv
import requests
import json

"""This module reads the exam for the Python II Hack University class and saves the answers.
For example:

$ len(exam.QUESTIONS)
>>>11

"""

default_path = os.path.join(os.getcwd(),'exam.csv')
default_url = 'https://raw.githubusercontent.com/hackoregon/civicu-pythonii-summer-2017/ceasar/lessons/shared-resources/exam.csv'

QUESTIONS = []
QUESTION_TEXTS = []
ANSWERS = []
MY_ANSWERS = ["B","D","B","ACF","AF","AEG","ABCDEF","B","CD","B","ABCDEFG"]
MY_ANSWERS_JS = '[{"answer": "B", "id": 0}, {"answer": "D", "id": 1}, {"answer": "B", "id": 2}, {"answer": "ACF", "id": 3}, {"answer": "AF", "id": 4}, {"answer": "AEG", "id": 5}, {"answer": "ABCDEF", "id": 6}, {"answer": "B", "id": 7}, {"answer": "CD", "id": 8}, {"answer": "B", "id": 9}, {"answer": "ABCDEFG", "id": 10}]'


def read_exam(filepath=default_path, url=False):
    """This function takes a file system path to a *.csv as input,
    opens it, extracts the first three columns as lists, and returns
    them in a 3-tuple of lists.
    To download the csv from a url, set url to True and insert the url as the filepath.
    """
    if url:
        csv_file = requests.get(filepath)
        print(csv_file.text)
    else:
        with open(filepath) as csv_file:
            file_reader = csv.reader(csv_file)
            csv_header = next(file_reader)
            # answer = [(row[0], row[1], row[2]) for row in file_reader]
            for row in file_reader:
                QUESTIONS.append(row[0])
                QUESTION_TEXTS.append(row[1])
                ANSWERS.append(row[2])
    return list(zip(QUESTIONS, QUESTION_TEXTS, ANSWERS))

def create_answer_js():
    final_list = [dict(zip(['id','answer'], [quest,ans])) for quest, ans in zip(QUESTIONS, ANSWERS)]
    return json.dumps(final_list)
