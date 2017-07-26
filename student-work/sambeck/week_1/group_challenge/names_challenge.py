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


class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def ask_a_question(self, question):
        print('42')


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


def names_func(a_list, size):
    shuffle(a_list)
    outlist = []
    while len(a_list):
        if len(a_list) >= size:
            team = []
            for i in range(size):
                team.append(a_list.pop())
            outlist.append(team)
        elif len(a_list) == 1:
            outlist[0] += a_list
            break
        else:
            outlist.append(a_list)
            break

    return outlist


if __name__ == '__main__':
    # Any code here will run when you run the command:
    # `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))
