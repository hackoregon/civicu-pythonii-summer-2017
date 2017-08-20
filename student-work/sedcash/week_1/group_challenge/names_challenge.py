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
    def __init__(self, first_name, last_name, email, question):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.question = question
    def ask_a_question(self,question):
        print(question)




class Student(Person):
    def __init__(self, first_name, last_name, email, question, book_dict = None, book_id = 0):
        super.__init__(self, first_name, last_name,email, question)
        if book_dict == None:
            self.book_dict = {}
        else:
            self.book_dict = book_dict

        self.book_id = book_id

    def add_book(self, book):
        self.book_dict[self.book_id] = book
        self.book_id += 1
    def remove_book(self, book):
        del self.book_dict[book]

    def show_books(self):
        print(self.book_dict)

class Teacher(Person):
    def __init__(self, first_name, last_name, email, question, student_list = None):
        super.__init__(self, first_name, last_name,email, question)
        if student_list == None:
            self.student_list = []
        else:
            self.book_dict = student_list



def names_func(a_list, size):
    mix_names = []
    for i in a_list:
        mix_names.append([random.choice(a_list)] * size)
        mix_names.remove(random.choice(a_list))
    return mix_names


print(names_func(["one", "two", "three", "four", "five"], 2))
