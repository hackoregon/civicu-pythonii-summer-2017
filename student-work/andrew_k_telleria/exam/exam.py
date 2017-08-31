import csv
import requests
from pprint import pprint
import json

QUESTIONS = []
QUESTION_TEXTS = []
ANSWERS = []

def read_exam(path):
	global QUESTIONS
	global QUESTION_TEXTS
	global ANSWERS

	with open(path) as fin:
		freader = csv.reader(fin)
		hrow  = next(freader)
		exam_tuple = ([],[],[])

		for row in freader:
			exam_tuple[0].append(row[0])
			exam_tuple[1].append(row[1])
			exam_tuple[2].append(row[2])


		# pprint(exam_tuple)
		QUESTIONS = exam_tuple[0]
		QUESTION_TEXTS = exam_tuple[1]
		ANSWERS = exam_tuple[2]
		return exam_tuple, QUESTIONS, QUESTION_TEXTS, ANSWERS





read_exam('../../../lessons/shared-resources/exam.csv')


MY_ANSWERS = ['B','D','B','ACF','AF','AGE','ABCDEF','B','CD','B','ABCDEFG']
MY_ANSWER_JS = [{"id": int(q), "my_answer": a} for q, a in zip(QUESTIONS, ANSWERS)]


pprint(json.dumps(MY_ANSWER_JS))



