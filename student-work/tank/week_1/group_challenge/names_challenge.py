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
class people:
    def __init__(self, first_name,last_name,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def ask_a_question(self):
        pass

class student(people):
    def __init__(self, name,last,email):
        super().__init__(name,last,email)
        self.books = {}

    def add_book(self,book,price):
        self.books[book] = price
    def remove_book(self,book):
        print(f'Removing {book}')
        self.books.pop(book,None)
    def show_books(self):
        print(self.books)

class teacher(people):
    def __init__(self, name,last,email):
        super().__init__(name,last,email)
        self.student_list = []
    def shuffle_class(self, a_list, size):
        """
        This func should take a list and size, break the list into lists of the
        size and return a list of lists.
        Size can not be less than 2.
        """
        listoflists = []
        for i in range(0, len(a_list)):
            dim = int(i/size)
            if len(a_list)-1==i:
                if len(a_list)%size==1:
                    dim = int(i/size)-1
            elif i%size==0:
                listoflists.append([])
            listoflists[dim].append(a_list[i])
        return listoflists
    def add_student(self,name):
        self.student_list.append(name)
    def remove_student(self,student):
        self.student_list.remove(student)
        print(f'Removing {student}')
    def show_students(self):
        print(self.student_list)


if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    teacher1 = teacher('prof','last','name@com.com')
    names= []
    students = {}
    student1 = student('fred','flintstone','fred@com.com')
    student2 = student('wilma','flintstone','fred@com.com')
    student3 = student('pebbles','flintstone','fred@com.com')
    student4 = student('dino','flintstone','fred@com.com')
    teacher1 = teacher('kazoo','flintstone','wilma@com.com')
    teacher1.add_student(student1.first_name)
    teacher1.add_student(student2.first_name)
    teacher1.add_student(student3.first_name)
    teacher1.add_student(student4.first_name)
    # for i in range(1,11):
    #     names.append(f'Student_{i}')
    #     students[names[i]] = student('names[i]','last','name@com.com')
    #     teacher1.add_student()
    print(teacher1.shuffle_class(teacher1.student_list, 2))
    teacher1.show_students()
    teacher1.remove_student('dino')
    teacher1.show_students()
    student1.add_book('Revolt 2100',1)
    student1.add_book('Web of Debt',2)
    student1.add_book('Frozen Republic',3)
    student1.add_book('Automate the Boring Stuff',4)
    student1.show_books()
    student1.remove_book('Web of Debt')
    student1.show_books()

