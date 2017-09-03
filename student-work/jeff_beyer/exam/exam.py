import doctest
import json
import pandas as pd

'''
Exam submission for Pythonii - Jeff Beyer - 08/30/2017
'''


def read_exam(csv_location='exam.csv'):
    '''
    read_exam will pull the exam.csv file from either an file path or a URL.
    If no input is given, it will default to looking for exam.csv in the
    current folder.

    Doctest if an invalid path is given:

    >>> read_exam('invalid_file.csv')
    ('', '', '')
    '''
    try:
        # Read the csv as a data frame
        df = pd.read_csv(csv_location)
        # Pull the desired columns
        info = (list(df['question number']), list(df['question']),
                list(df['answer']))
    except:
        # If we didn't read anything, return an empty 3-tuple
        info = ('', '', '')
    return info


def setup():
    '''
    Doctests for checking the length of the 4 lists:

    >>> len(QUESTIONS)
    11
    >>> len(ANSWERS)
    11
    >>> len(QUESTION_TEXTS)
    11
    >>> len(MY_ANSWERS)
    11
    '''
    # Read the exam file from web URL
    exam_info = read_exam('https://raw.githubusercontent.com/hackoregon/' +
                          'civicu-pythonii-summer-2017/ceasar/lessons/' +
                          'shared-resources/exam.csv')
    # Read the exam file from the local directory
    # exam_info = read_exam('exam.csv')
    # Read the exam file (without input)
    # exam_info = read_exam()

    # Store the exam info as global variables
    globals()['QUESTIONS'] = exam_info[0]
    globals()['QUESTION_TEXTS'] = exam_info[1]
    globals()['ANSWERS'] = exam_info[2]

    # Store my answers and a JSON string of my answers as global variables
    globals()['MY_ANSWERS'] = ['B', 'D', 'B', 'ACF', 'AF', 'AEG', 'ABCDEF',
                               'B', 'CD', 'B', 'ABCDEFG']
    globals()['MY_ANSWERS_JS'] = (
        json.dumps([{'id': ind, 'my_answer': val} for ind, val in
                   enumerate(globals()['MY_ANSWERS'])], indent=0))


# Run the setup function to define the global variables
setup()

if __name__ == "__main__":
    # Run the doctests
    doctest.testmod()
