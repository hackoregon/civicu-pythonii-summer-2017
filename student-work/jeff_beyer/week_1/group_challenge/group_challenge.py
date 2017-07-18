import random

class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def ask_a_question(self, question):
        print(f'Q: {question}')

class Student(Person):

    def __init__(self, first_name, last_name, email, books):
        super().__init__(first_name, last_name, email)
        self.books = books

    def add_book(self, book):
        print(f'Adding {book} to book list.')
        self.books.append(book)

    def remove_book(self, book):
        print(f'Removing {book} from book list....', end='')
        if book in self.books:
            self.books.remove(book)
            print('REMOVED')
        else:
            print(f'ERROR\n{book} not found!')

    def show_books(self):
        print(f'Book list: {self.books}')

class Teacher(Person):

    def __init__(self, first_name, last_name, email, student_list):
        super().__init__(first_name, last_name, email)
        self.students = student_list

    def shuffle_class(self, group_size):
        """
        This func should take a list and size, break the list into lists of the
        size and return a list of lists.
        """
        # Make a copy so we don't erase our student list
        a_list = self.students[:]

        # Shuffle the names
        random.shuffle(a_list)  

        # Init the groups list (expected to be a list of lists)
        groups = list()

        while len(a_list) >= group_size:
            # Add the first size elements into our groups list, keep doing that
            # until we have less than size elements left
            groups.append(a_list[:group_size])
            a_list = a_list[group_size:]

        # If we have not zero elements left, we need to deal with them
        if len(a_list) != 0:
            # If it's only one element, add it to the last group
            if len(a_list) == 1:
                groups[-1].append(a_list[0])
            # Otherwise, just make it another group
            else:
                groups.append(a_list)

        return groups

Jeff = Student('Jeff', 'Beyer', 'jb@gmail', ['Dynamics','Statics','Materials'])
Jeff.show_books()
Jeff.add_book('Traffic')
Jeff.show_books()
Jeff.remove_book('Cars')
Jeff.show_books()
Jeff.remove_book('Dynamics')
Jeff.show_books()

Teach = Teacher('Jf', 'By', 'j@gm', ['Fred', 'Nick', 'Bob','Jill','Joe','Kim',
    'Tom','Mike','Anon','Eulid','Kipchogee','Bill','Allison','Mary','Alex'])
print(Teach.students)
print(Teach.shuffle_class(2))
print(Teach.shuffle_class(4))
print(Teach.shuffle_class(4))
print(Teach.shuffle_class(4))