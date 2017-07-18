
class BaseClass:

    def __init__(self, first_name, last_name, email, question):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.question = question

    def ask_a_question(self):
        return(self.question)


class Student(BaseClass):

    def __init__(self, first_name, last_name, email, question, books_add, books_remove):
        super().__init__(first_name, last_name, email, question)
        self.books_dict = {}
        self.books_add = books_add
        self.books_remove = books_remove

    def add_book(self):
        for book in self.books_add:
            if book in self.books_dict.keys():
                self.books_dict[book] =+ 1
            else:
                self.books_dict[book] = 1
        return(self.books_dict)

    def remove_book(self):
        for book in self.books_remove:
            if self.books_dict[book] > 1:
                self.books_dict[book] -= 1
            else:
                del self.books_dict[book]
        return(self.books_dict)

    def show_books(self):
        return(self.books_dict.keys())


class Teacher(BaseClass):
    def __init__(self, first_name, last_name, email, question, student_list, size):
        super().__init__(first_name, last_name, email, question)
        self.student_list = student_list
        self.size = size

    def shuffle_class(self):

        from group_challenge.names_challenge import names_func

        output = names_func(self.student_list, self.size)
        return output


if __name__ == '__main__':
    student1 = Student('first', 'last', 'email','q', ['b1', 'b2', 'b3'],['b2'])
    teacher1 = Teacher('first', 'last', 'email','q', list(range(18)), 5)
    print(student1.ask_a_question())
    print(student1.add_book())
    print(student1.remove_book())
    print(student1.show_books())
    print(teacher1.shuffle_class())