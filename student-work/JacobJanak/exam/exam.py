import os
import requests
import csv
import re
from urllib.parse import urlparse
import json


def read_exam(url_or_path):
    """ Checks if the string argument is
    a url or a relative file path and then
    calls the corresponding function. """

    # check if it's a valid url
    if urlparse(url_or_path).netloc:
        return url_to_csv(url_or_path)

    # check if it's an existing file
    path = os.path.abspath(url_or_path)
    if os.path.exists(path):
        return path_to_csv(path)

    # if not raise an error
    else:
        raise AttributeError('Not a valid url or relative file path.')


def url_to_csv(url):
    """ Uses 'requests' to get raw text from the web page
    and then manually creates a list of rows which each
    contain a list of columns. 'urllib' wouldn't work because
    of security blocks and using 'csv' to turn data into lists
    resulted in very very poor formatting. """

    # get text of webpage at the url
    page = requests.get(url).text.strip()

    # create table as a list of lists (manually do what 'csv' should do)
    table = page.split('\n')
    for i, row in enumerate(table):

        # splits string by ',' but not between quotes
        table[i] = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', row)

        # remove quotes that were used to escape column delimeters
        table[i] = [column.replace('"', '') for column in table[i]]

    return homework_tuple(table)


def path_to_csv(path):
    """ Reads the file that we already know exists
    and turns that data into a list of lists. """

    # open the file and convert it to reader object
    with open(path) as f:
        reader = csv.reader(f)

        # coerce reader object into list for list methods
        return homework_tuple(list(reader))


def homework_tuple(table):
    """ Creates 3 lists and adds data to them as we loop
    through the table then returns them as a tuple. """

    # NOTE: adjust as needed to dynamically get column indicies
    header = table.pop(0) # also removes row[0] so we don't get errors
    number_index = header.index('question number')
    question_index = header.index('question')
    answer_index = header.index('answer')

    # iterate through table and append values to lists
    numbers, questions, incorrects = [], [], []
    for row in table:
        numbers += [row[number_index]]
        questions += [row[question_index]]

        # add only the incorrect answers to list by checking the answer columns value
        for i, column in enumerate(row[answer_index + 1:]):
            if header[i + answer_index + 1] not in row[answer_index]:
                incorrects += [column]

    return (numbers, questions, incorrects)

def list_to_json_with_index(l):
    """ Takes a list and converts it to a string
    of json with an additional column 'id' """

    # use enumerate to create the id and append to string
    json_string = '['
    for i, answer in enumerate(l):
        json_string = json_string + '{"id":%s,"my_answer":"%s"},' % (i, answer)

    # replace final comma with a closing bracket
    return json_string[:-1] + ']'


# UNCOMMENT TO SEE THE RESULTS
# print(read_exam('https://raw.githubusercontent.com/hackoregon/civicu-pythonii-summer-2017/master/lessons/shared-resources/exam.csv'))
# print(read_exam('exam.csv'))

result = read_exam('exam.csv')

global QUESTIONS
global QUESTION_TEXTS
global ANSWERS
global MY_ANSWERS
global MY_ANSWERS_JS

QUESTIONS = result[0]
QUESTION_TEXTS = result[1]
ANSWERS = result[2]
MY_ANSWERS = ['B', 'D', 'BE', 'ACF', 'AF', 'AEG', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']
MY_ANSWERS_JS = list_to_json_with_index(MY_ANSWERS)
