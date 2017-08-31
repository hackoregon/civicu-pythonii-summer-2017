'''
python II exam - sam beck
'''
import pickle
import json


def read_exam(filepath='../../lessons/shared-resources/exam.csv'):
    '''
read_exam takes the path to this exam and returns 3 lists as
a truple with elements:
1. question numbers
2. question strings
3. list of incorrect answers
>>> type(read_exam())
tuple
    '''
    if filepath.startswith('http'):
        return 'maybe just downlod this file'

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

        # while True:
        for i in range(11):
            try:
                dirtyline = f.readline().strip().split(',')
                line = [str(e).strip("\"") for e in dirtyline]
                # print(line)
                question_numbers.append(line[0])
                question_text.append(line[1])
                possibly_random_letters.append(line[2])

                print(line[1])
                print('coded answer?', line[2])
                print('answers', line[3:])
                my_answers.append('')
                incorrect_answers.append([])
                for i in range(3, len(line)):
                    answer_is_correct = input(line[i])
                    if not answer_is_correct:  # because we want incorrect
                        incorrect_answers[-1].append(line[i])
                    else:
                        my_answers[-1] = my_answers[-1] + header[i]

            except IndexError:
                print('out of lines')
                break

    with open('answers.pkl', 'wb') as outf:
        for lst in [question_numbers, question_text,
                    incorrect_answers, my_answers]:
            pickle.dump(lst, outf)

    return (question_numbers, question_text, incorrect_answers), my_answers


def load_all():
    with open('answers.pkl', 'rb') as f:
        QUESTIONS = pickle.load(f)
        QUESTION_TEXTS = pickle.load(f)
        ANSWERS = pickle.load(f)
        MY_ANSWERS = pickle.load(f)

        l = []
        for i in range(11):
            # print(i)
            l.append({QUESTIONS[i]: MY_ANSWERS[i]})
        MY_ANSWERS_JS = json.dumps(l)

        # print(json.loads(MY_ANSWERS_JS))

        return QUESTIONS, QUESTION_TEXTS, ANSWERS, MY_ANSWERS, MY_ANSWERS_JS


if __name__ == '__main__':
    try:
        QUESTIONS, QUESTION_TEXTS, ANSWERS, MY_ANSWERS, MY_ANSWERS_JS = load_all()
    except IOError:
        print('pickle is missing, so you should do test yourself.')
        read_exam()
