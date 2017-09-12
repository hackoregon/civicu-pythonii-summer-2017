import csv
import os
import json


QUESTIONS = []
ANSWERS = []
QUESTIONS_TEXTS = []
MY_ANSWERS = ['B','D','B','ACF','AF','AGE','ABCDEF','B','CD','B','ABCDEFG']
MY_ANSWERS_JSON = [{'index': int(k), "answer(s)": y} for k,y in zip(QUESTIONS,ANSWERS)]

#abs_path = '/home/cassandra/Projects/civicu-pythonii-summer-2017/lessons/shared-resources/exam.csv'
cwd = os.getcwd()
csv_file = 'exam.csv'
datafile = os.path.join(cwd,csv_file)

def read_exam(datafile):
    ''' read_exam() function should return 3 lists in a 3-tuple of lists.
    First object in the tuple: list of the question numbers from the exam.CSV file
    Second object in the tuple: list of the question text strings from the exam.CSV file
    Third object in the tuple: list of the correct answers to the questions from the exam.CSV file
    '''

    with open(datafile, 'r') as f:
        exam_reader = csv.reader(f)
        new_list = list(map(tuple, exam_reader))[1:]
        #print(list(new_list))

        for row in new_list:
            QUESTIONS.append(row[0])
            QUESTIONS_TEXTS.append(row[1])
            ANSWERS.append(row[2])
        #print(QUESTIONS)
        #print(QUESTIONS_TEXTS)
        #print(ANSWERS)
        return(QUESTIONS,QUESTIONS_TEXTS,ANSWERS)


#loads() turn a JSON-encoded string back into a Python data structure:
def json_encoded_string():
    string = [{'index': int(k), "answer(s)": y} for k,y in zip(QUESTIONS,ANSWERS)]
    return json.dumps(string)

