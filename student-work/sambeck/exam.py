'''
python II exam - sam beck
'''


def read_exam(filepath='../../lessons/shared-resources/exam.csv',
              user_input=False):
    '''
read_exam takes the path to this exam and returns 3 lists as
a truple with elements:
1. question numbers
2. question strings
3. list of incorrect answers
>>> type(read_exam())
tuple
    '''
    with open(filepath) as f:
        question_numbers = []
        question_text = []
        possibly_random_letters = []
        incorrect_answers = []
        my_answers = []
        print('header:')
        header = f.readline().split()

        for i in range(1):
            t_f_sequence = []
            try:
                line = f.readline().split(',')
                # print(line)
                question_numbers.append(line[0])
                question_text.append(line[1])
                possibly_random_letters.append(line[2])

                print(line[1])
                print('coded_answer?', line[2])
                for i in range(3, len(line)):
                    answer_is_correct = input(line[i])
                    my_answers.append('')
                    if not answer_is_correct:  # because we want incorrect
                        incorrect_answers.append(line[i])
                        t_f_sequence.append(False)
                    else:
                        t_f_sequence.append(True)
                        my_answers[-1] += header[i]
            except IndexError:
                print('out of lines')
                break

        if user_input:
            return t_f_sequence
        else:
            return (question_numbers, question_text, incorrect_answers), my_answers
