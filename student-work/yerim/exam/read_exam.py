import csv
import requests
import os
import json

QUESTIONS = list()
QUESTION_TEXTS = list()
incorrect_answers = list()
# MY_ANSWERS = ['B', 'D', 'B', 'ACF', 'AF', 'AGE', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']
encrypted_answers = []

def read_exam(url_or_path):

    # url
    if 'https' in url_or_path:
        requests.get(url_or_path)

    # local
    full_path = url_or_path.split(os.sep)
    path = os.sep.join(full_path[:-1])
    if path is '':
        full_path = [url_or_path]
    else:
        os.chdir(path)

    with open(full_path[-1]) as exam_csv:
        my_reader = csv.reader(exam_csv)
        header = next(my_reader)
        for row in my_reader:
            QUESTIONS.append(row[0])
            QUESTION_TEXTS.append(row[1])
            incorrect_answers.append(row[-1])
            encrypted_answers.append(row[2])

    return tuple([QUESTIONS, QUESTION_TEXTS, incorrect_answers])


def decrypt(string):
    rot = 13
    output = ''
    for letter in string:
         output += chr((ord(letter) - ord('A') + rot) % 26 + ord('A'))
    return output


# decrypt from the encrypted answer to get the right answer
MY_ANSWERS = []
for ans in encrypted_answers:
    MY_ANSWERS.append(decrypt(ans))


# convert to json
MY_ANSWERS_JS = []
lst1 = list(zip(['id']*len(QUESTIONS), QUESTIONS))
lst2 = list(zip(['my_answer']*len(MY_ANSWERS), MY_ANSWERS))
for i in range(len(lst1)):
    d={}
    d[lst1[i][0]] = int(lst1[i][1])
    d[lst2[i][0]] = lst2[i][1]
    MY_ANSWERS_JS.append(d)

MY_ANSWERS_JS = json.dumps(MY_ANSWERS_JS)

