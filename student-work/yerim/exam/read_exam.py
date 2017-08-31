import csv
import requests
import os

questions = []
text_str = []
incorrect_answers = []

def read_exam(url_or_path):
    # # url
    # if 'https' in url_or_path:
    #     requests.get(url_or_path)

    # local
    path = url_or_path.split(os.sep)
    path = os.sep.join(path[:-1])
    os.chdir(path)

    with open(path[-1]) as exam_csv:
        my_reader = csv.reader(exam_csv)
        header = next(my_reader)
        questions = list()
        # text_str = list()
        # incorrect_answers = list()
        for row in my_reader:
            questions = questions.extend(row[0])
            # text_str = text_str.extend(row[1])
            # incorrect_answers = incorrect_answers.extend('c')


    return tuple(questions, text_str, incorrect_answers)

read_exam('exam.csv')