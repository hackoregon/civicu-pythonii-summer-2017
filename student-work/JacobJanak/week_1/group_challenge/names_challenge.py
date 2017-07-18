""" 
The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists matches the bin size.

For example calling the function with a list of names and the size of 2 should return
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is
remaining add that name to another inner list.
"""

from random import shuffle
import math


class Person:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def ask_question(self, question):
        print(self.name + " asks " + question)


class Student(Person):
    def __init__(self, first, last, email, books, teacher):
        super().__init__(first, last, email)
        self.books = set(books)
        self.teacher = teacher
        teacher.addStudent(self)

    def addBook(self, book):
        self.books.add(book)

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print('cannot remove')

    def showBooks(self):
        print(self.books)


class Teacher(Person):
    def __init__(self, first, last, email):
        super().__init__(first, last, email)
        self.studentList = []

    def addStudent(self, student):
        self.studentList.append(student)


def names_func(list, size):
    shuffle(list)

    team_count = math.ceil((len(list)-1)/size)

    result = []
    for i in range(team_count):
        result.append(list[size*i:size*(i+1)])

    if len(list) - team_count * size == 1:
        result[0].append(list[-1])

    return result


    """ This method is more practical for real life
    shuffle(list)

    team_count = math.ceil((len(list)-1)/size)

    final = []
    for i in range(team_count):
        final.append([])

    i = 0
    for student in list:
        final[i].append(student)
        if i == team_count - 1:
            i = 0
        else:
            i += 1

    return final

    """

if __name__ == '__main__':
    # Any code here will run when you run the command:
    # `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))
