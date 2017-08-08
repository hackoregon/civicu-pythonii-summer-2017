class BaseClass:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def ask_a_question(self, question):
        print(question)

class Student(BaseClass):
    def __init__(self, first_name, last_name, email, books_dict={}):
        super().__init__(first_name, last_name, email)
        self.books_dict = {}
        #self.teacher = teacher
        #teacher.add_student(self)

    def add_book(self, book_name, author):
        self.books_dict[book_name] = author

    def remove_book(self, book_name):
        try:
            del self.books_dict[book_name]
        except KeyError:
            print("That book is not in the dictionary.")

    def show_books(self):
        print(self.books_dict)

class Teacher(BaseClass):
    def __init__(self, first_name, last_name, email, student_list=[]):
        super().__init__(first_name, last_name, email)
        self.student_list = student_list

    def shuffle_class(self, size):
        from group_challenge.names_challenge import names_func
        shuffled = names_func(self.student_list, size)
        print(shuffled)

if __name__ =='__main__':
    Ashley = Student('ashley', 'riehl', 'ashley_riehl@hotmail.com', {})
    Ashley.add_book("Summer", "Winter")
    Ashley.add_book("Fall", "Spring")
    Ashley.remove_book("Summer")
    Ashley.add_book("Book2", "Author2")
    Ashley.show_books()

    Teacha = Teacher('Math', 'Teacher', 'teacher@school.us', list(range(20)))
    Teacha.shuffle_class(2)
