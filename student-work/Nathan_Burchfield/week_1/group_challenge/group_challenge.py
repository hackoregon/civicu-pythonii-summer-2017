"""
The goal of this challenge is to create a function that will take a list of
names and a bin size and then shuffle those names and return them in a
list of lists where the length of the inner lists matches the bin size.

For example calling the function with a list of names and the size of 2 should return
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is
remaining add that name to another inner list.
"""

import re
import random


class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def info(self, email):
        if re.search('@.+', email).group():
            print(f"{self.first_name}'s email: {email} is valid.")
        else:
            print("Email not valid")

    def questions(self, question):
        print(f"This is the question:{question}")


class Teacher(Person):

    """Represents the teachers."""

    def __init__(self, first_name, last_name, email, sudent_list):
        super().__init__(first_name, last_name, email)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.student_list = student_list

    def shuffle_class(self,student_list, size):
        random.shuffle(student_list)

        random_student_list = [student_list[i:i + size] for i in range(0, len(student_list), size)]

        if len(random_student_list[-1]) == 1:
            random_student_list[-2].append(random_student_list[-1][0])

            random_student_list.pop()

        return random_student_list

    def info(self, email):
        super().info(email)
        if re.search('@.+', email).group():
            print("")
        else:
            print("Email not valid")


class Student(Person):

    """Represents a student."""

    def __init__(self, first_name, last_name, email, book_collection):
        super().__init__(first_name,last_name,email)
        self.book_collection = {}

    def add_book(self,book,author):
        print(f"Adding {book} {author}'s book to {self.first_name}'s book collection.")
        self.book_collection[book] = author

    def remove_book(self, book,author):
        print(f"{book} by {author} has been taken out of the collection", end=' ')
        if book in book_collection:
            del[book]
            print(f"{self.first_name}'s book collection")
        else:
            print(f"This book is not in {self.first_name}'s collection.{book}{author}")

    def show_book(self):
        print(f"{self.first_name}'s book collection:{book_collection}")

    def info(self, email):
        super().info(email)
        if re.search('@.+', email).group():
            print("")
        else:
            print("Email not valid")

student_list = ['Andrew', 'Nate', 'John', 'Katie', 'Gina', 'Megan', 'Trent']
f = Teacher("Ted", "Donald", "TD@gmail.com", student_list)
f.info("TD@gmail.com")
book_collection = {"Cat's Cradle", 'Kurt Vonnegut'}
s = Student("Bartholomew", "Smith", "BS@gmail.com", book_collection)
s.info("BS@gmail.com")
s.show_book()
s.add_book('The Prince', 'Machiavelli')
s.remove_book("Cat's Cradle", 'Kurt Vonnegut')
print(f.shuffle_class(student_list, 2))


if __name__ == '__main__':

    # Any code here will run when you run the command: `python names_challenge.py`

    pass


