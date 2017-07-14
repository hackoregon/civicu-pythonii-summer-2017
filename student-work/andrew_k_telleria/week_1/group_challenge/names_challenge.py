"""
The goal of this challenge is to create a function that will take a list of
names and a bin size and then shuffle those names and return them in a
list of lists where the length of the inner lists matches the bin size.

For example calling the function with a list of names and the size of 2 should return
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is
remaining add that name to another inner list.
"""
import random

class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def ask_a_question(self):
        print('{} asked a question.'.format(self.first_name))


class Student(Person):
    def __init__(self, first_name, last_name, email, books_dict):
        super().__init__(first_name, last_name, email)
        self.books_dict = books_dict
    books_dict = {}

    def add_book(self, book_name, author):
        books_dict[book_name] = author
        return books_dict

    def remove_book(self, book_name):
        del books_dict[book_name]
        return books_dict

    def show_books(self):
        print(books_dict)



class Teacher(Person):
    def __init__(self, first_name, last_name, email, student_list):
        super().__init__(first_name, last_name, email)
        self.student_list = student_list

    def shuffle_class(self, student_list, size):
        random.shuffle(student_list)
        random_student_list = [student_list[i:i + size] for i in range(0, len(student_list), size)]
        if len(random_student_list[-1]) == 1:
            random_student_list[-2].append(random_student_list[-1][0])
            random_student_list.pop()
        return random_student_list

student_list = ['Andrew', 'Nate', 'John', 'Katie', 'Gina', 'Megan', 'Trent']
books_dict = {'Automate The Boring Stuff': 'Python II'}
teacher1 = Teacher('Zak', 'Kent', 'zak@hackoregon.org', student_list)
student1 = Student('Andrew', 'Telleria', 'atelleria08@gmail.com', books_dict)
print(teacher1.shuffle_class(student_list, 2))
print(student1.add_book('The Thing of Darkness', 'Harry Thompson'))
print(student1.remove_book('The Thing of Darkness'))
print(student1.show_books())



if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    pass
