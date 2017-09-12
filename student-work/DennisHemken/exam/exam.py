import pprint
import json
import pandas as pd
import doctest

'''
Exam Python Module
'''

QUESTIONS = []
QUESTION_TEXTS = []
ANSWERS = []
MY_ANSWERS = []
MY_ANSWERS_JS = []

def read_exam(exam_location = 'exam.csv'):
    
    
    '''
    read_exam will read in the exam.csv file from the given path.
    If no path is given, it will default to trying exam.csv in the 
    current working directory.
    
    Doctest to see if we have a valid csv location
    
    >>> read_exam('invalid_location.csv')
    ('','','')
    '''
    
    try:
        #Read in as a dataframe
        dataframe = pd.read_csv(exam_location)
        
        question_numbers = list(dataframe['question number'])
        question_text = list(dataframe['question'])
        incorrect_answers = list(dataframe['answer'])
        exam_overview = (question_numbers, question_text, incorrect_answers)

    except IOError:
        #If no file was read in, return an empty tuple
        exam_overview = ([],[],[])
        
            
    return exam_overview

def setup():
    global QUESTONS
    global QUESITON_TEXT
    global ANSWERS
    global MY_ANSWERS
    global MY_ANSWERS_JS
    
    '''
    Doctests for checking the lengths of the 4 lists
    
    >>>len(question_numbers)
    11
    >>>len(incorrect_answers)
    11
    >>>len(question_text)
    11
    >>>len(my_answer)
    11
    '''
    
    #Read in the exam from exam.csv
    exam_info = read_exam('https://raw.githubusercontent.com/hackoregon/' +
                          'civicu-pythonii-summer-2017/ceasar/lessons/' +
                          'shared-resources/exam.csv')
    
    #store exam info as global variables
    QUESTIONS = exam_info[0]
    QUESITON_TEXT = exam_info[1]
    ANSWERS = exam_info[2]
    
    #store my answers as a global variable
    MY_ANSWERS = ['B', 'D', 'B', 'ACF', 'AF', 'AEG', 'ABCDEF', 'B', 'CD', 'B', 'ABCDEFG']
    MY_ANSWERS_JS = (
            json.dumps([{'id': i, 'my_answer': a} for (i, a) in
                        enumerate(MY_ANSWERS)], indent=2))
    
    #Run setup function to define the global variables
    setup()
    
    if __name__=="__main__":
        #Run doctests
        doctest.testmod()
        
    