'''
python II exam - sam beck
'''
import pickle
import json


def read_exam(filepath='../../lessons/shared-resources/exam.csv', inter=True):
    '''
read_exam is an interactive test_taking program.
a list of correct answers is saved to a pickle; load it with make_answers()

ARGS:
  filepath: string: path to test .csv, default is exam.csv in shared-resources
  inter: bool: whether test is interactive. default is true, false for testing

RETURNS:
  3-tuple: (question_numbers, question_text, incorrect_answers)
    '''

    if filepath.startswith('http'):
        return 'maybe just download the file?'

    with open(filepath) as f:
        question_numbers = []
        question_text = []
        possibly_random_letters = []
        incorrect_answers = []
        my_answers = []
        print('header:')
        dirtyheader = f.readline().strip().split(',')
        header = [str(e).strip("\"") for e in dirtyheader]
        print(header)
        print()
        if inter:
            print('enter 1 for true answers. enter 0 (or _) for false answers')
        else:
            print('exam running in auto-mode')

        # while True:
        for i in range(11):
            try:
                dirtyline = f.readline().strip().split(',')
                line = [str(e).strip("\"") for e in dirtyline]
                # print(line)
                question_numbers.append(int(line[0]))
                question_text.append(line[1])
                possibly_random_letters.append(line[2])

                print()
                print(line[0], '=> ', line[1])
                print('coded answer(s):', line[2])
                print('answer choices:', line[3:])
                my_answers.append('')
                incorrect_answers.append([])
                for i in range(3, len(line)):
                    # inter is true by default, false when run in exam_tests
                    if inter:
                        answer_is_correct = input(line[i])
                    else:
                        answer_is_correct = i % 2  # simulate input for test

                    if not answer_is_correct:  # we want incorrect answers
                        incorrect_answers[-1].append(line[i])
                    else:
                        my_answers[-1] = my_answers[-1] + header[i]

            except IndexError:
                print('out of lines')
                break

    if inter:
        outfile = 'answers.pkl'
    else:
        outfile = 'test_answers.pkl'  # so real answers are not saved over

    with open(outfile, 'wb') as f:
        # dump questions and answers to pickle
        for lst in [question_numbers, question_text,
                    incorrect_answers, my_answers]:
            pickle.dump(lst, f)

    # return only the tuple
    return (question_numbers, question_text, incorrect_answers)


def make_answers(inter=True):
    '''
loads variables previously stored by read_exam

ARGS:
  inter: bool: interactive mode, true by default, false for test_make_answers

RETURNS:
  QUESTIONS, QUESTION_TEXTS, ANSWERS, MY_ANSWERS: lists spec'd by exam
  MY_ANSWERS_JS: string: json of answers set by input
'''
    if inter:
        infile = 'answers.pkl'
    else:
        infile = 'test_answers.pkl'

    with open(infile, 'rb') as f:
        QUESTIONS = pickle.load(f)
        QUESTION_TEXTS = pickle.load(f)
        ANSWERS = pickle.load(f)
        MY_ANSWERS = pickle.load(f)

        l = []
        for i in range(11):
            # print(i)
            l.append({QUESTIONS[i]: MY_ANSWERS[i]})
        MY_ANSWERS_JS = json.dumps(l)

        return QUESTIONS, QUESTION_TEXTS, ANSWERS, MY_ANSWERS, MY_ANSWERS_JS


if __name__ == '__main__':
    try:
        QUESTIONS, QUESTION_TEXTS, ANSWERS,\
            MY_ANSWERS, MY_ANSWERS_JS = make_answers()
    except IOError:
        print('pickled answers do not exist; you need to take the test.')
        read_exam()
        QUESTIONS, QUESTION_TEXTS, ANSWERS,\
            MY_ANSWERS, MY_ANSWERS_JS = make_answers()
