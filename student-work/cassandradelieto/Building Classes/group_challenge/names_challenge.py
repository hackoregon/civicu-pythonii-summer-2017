import random
import math

class Person(self): #base class for shared characteristics amongst all classes.
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    #def ask_a_question(self): #I don't get what this is supposed to do?
        #return(pass)

class Student(Person):
    def __init__(self, first_name, last_name, email, book, teacher):
        self.book = book
        self.teacher = teacher
        self.books_dict = []

    def add_book(self, book): #this method will add a book to the student's books_dict.
        self.book.add(book)

    def remove_book(self, book):
        self.book.remove(book)

    def show_books(self):
        print(self.book)


class Teacher(Person): #Student will inherit Teacher's methods so it will become a super().__init__
    def __init__(self, first_name, last_name, email):
        self.student_list = [] #creates a list of student names

    def shuffle_class(self, list):


def names_func(a_list, size):
    """
    This func should take a list and size, break the list into lists of the
    size and return a list of lists.
    """

    a_list =

    size =

    return

if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))
