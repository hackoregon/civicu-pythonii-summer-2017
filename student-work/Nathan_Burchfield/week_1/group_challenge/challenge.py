import re


class Person:

    def __init__(self,first_name,last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def info(self, email):
        if re.search('@.+', email).group():
            print("%s's email is valid: %s." %(self.first_name,email))
        else:
            print("Email not valid")

    def q_time(self, question):
        print("%s" % question)


class Teacher(Person):

    """Represents the teachers."""

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
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
        self.book_collection = book_collection

    def add_book(self,book):
        print("Adding %s to %s's book collection." % (book, self.first_name))
        self.book_collection.append(book)

    def remove_book(self, book):
        print("%s has been taken out of " % book, end='')
        if book in self.book_collection:
            self.book_collection.remove(book)
            print("%s's collection." % self.first_name)
        else:
            print("This book is not in your collection\n :%s" % book)

    def libary(self):
        print("%s's book collection:%s" % (self.first_name,self.book_collection))

    def info(self, email):
        super().info(email)
        if re.search('@.+', email).group():
            print("")
        else:
            print("Email not valid")

f = Teacher("Ted", "Donald", "TD@gmail.com")
f.info("TD@gmail.com")
s = Student("Bartholomew", "Smith", "BS@gmail.com", ['Atlas Shrugged', 'Cats Cradle', '1984'])
s.info("BS@gmail.com")
s.libary()
s.add_book('Animal Farm')
s.libary()






