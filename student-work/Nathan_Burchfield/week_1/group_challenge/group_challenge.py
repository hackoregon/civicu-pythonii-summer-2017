import re


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
        print(f"Adding {book} to {self.first_name}'s book collection.")
        self.book_collection.append(book)

    def remove_book(self, book):
        print(f"{book} has been taken out of the collection", end=' ')
        if book in self.book_collection:
            self.book_collection.remove(book)
            print(f"{self.first_name}'s book collection")
        else:
            print(f"This book is not in {self.first_name}'s collection\n:{book}")

    def show_book(self):
        print(f"{self.first_name}'s book collection:{self.book_collection}")

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
s.show_book()
s.add_book('Animal Farm')
s.show_book()
s.remove_book('1984')






