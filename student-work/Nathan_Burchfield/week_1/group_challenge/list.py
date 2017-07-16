import re


class Teacher:

    """Represents the teachers."""

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.books =[]

    def info(self,first_name,last_name,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        if re.search('@.+', self.email).group():
            print(self.email)
        else:
            print("Email not valid")

    def reading(self):

        self = question = "Do you like to read?"
        print(self)

        answer = input("?")
        if answer == "yes":
            print("Great")
        else:
            print("You should read more.")


class Student(Teacher):

    """Represents a students."""

    def __init__(self, first_name, last_name, email):
        super(Student, self).__init__(first_name,last_name,email)
        return

    def info(self,first_name,last_name,email):
        super(Student, self).info(first_name,last_name,email)
        return

    def reading(self):
        super(Student, self).reading()
        return


class Book(Student):
    """Represents Student's books"""

    def __init__(self,first_name,last_name,email):
        super(Book, self).__init__(first_name,last_name,email)
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        b = re.split(r"(\w+)", book)

        answer = input("Do you want to remove any books from your list yes or no >?")
        if answer == 'yes':
            print(b)
            f = b.pop(-2)
            print(f)
        else:
            print(book)


a = Teacher("Bil","Bob","bob@Gmail.com")
a.info("Nathan","Bob","Nathan@gmail.com")

e = Student("Bob","Billy","bob@gmail.com")
e.info("Bob","Billy","bob@gmail.com")
e = Book("Bob","Billy","bob@gmail.com")
e.reading()
e.add_book("Shining Jaws ThePrince")







