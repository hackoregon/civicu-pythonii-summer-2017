import collections, random
""" 
The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists matches the bin size. 

For example calling the function with a list of names and the size of 2 should return 
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is 
remaining add that name to another inner list.
"""
class CourseMember:
    ''' CourseMember objects are all members of a particular course, either as students or teachers.
    This class assumes there's only one course, and everyone is a member of it '''
    student_list = []
    class_list = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def ask_a_question(self, s):
        print(s+"?")

    def __str__(self):
        if (self.last_name, self.first_name) in CourseMember.student_list:
            return "Name: " + self.first_name + " " + self.last_name + " (student); Email: " + self.email
        else:
            return "Name: " + self.first_name + " " + self.last_name + " (teacher); Email: " + self.email

    def print_class(self):
        for item in CourseMember.class_list:
            print(item)

	

class Teacher(CourseMember):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        CourseMember.class_list = [self] + CourseMember.class_list

    def student_list(self):
        return CourseMember.student_list

    def shuffle_class(self, work_group_size):
        '''shuffles students into workgroups
        Some workgroups will be of work_group_size. remaining students will be added to workgroups.
        So some workgroups will be one larger than work_group_size.'''
        students = self.student_list()
        random.shuffle(students)
        groups = [students[x:x+work_group_size] for x in range(0, len(students), work_group_size)]
        if len(groups) > 1:
           if len(groups[-2]) - len(groups[-1]) > 1:
                l = groups.pop()
                i = 0
                while len(l) > 0:
                    groups[i].append(l.pop())
                    i += 1
        return groups


class Student(CourseMember):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.books_dict = {}
        CourseMember.student_list.append((self.last_name, self.first_name))
        CourseMember.class_list.append(self)

    def add_book(self, book_author, book_title):
        if book_author in self.books_dict:
            self.books_dict[book_author].append(book_title)
        else:
            self.books_dict[book_author] = [book_title]

    def remove_book(self, book_author, book_title):
        if book_author not in self.books_dict:
            print("{} {} doesn't have {} by {}".format(self.first_name, self.last_name, book_author, book_title))
        else:
            if len(self.books_dict[book_author]) == 1:
                del self.books_dict[book_author]
            else:
                self.books_dict[book_author].remove(book_title)

    def show_books(self):
        print("{} {}'s books".format(self.first_name, self.last_name))
        for k, v in self.books_dict.items():
            print("-"*30)
            print("Book(s) by {}:".format(k))
            for item in v:
                print("\t" + item)


def names_func(a_list, size):
    """
    This func should take a list and size, break the list into lists of the
    size and return a list of lists.
    """
    random.shuffle(a_list)
    l = [a_list[x:x+size] for x in range(0, len(a_list), size)]
    if len(l[-1]) == 1:
        ll = l.pop()
        x = ll.pop()
        l[0].append(x)
    return l


if __name__ == '__main__':
    # Any code here will run when you run the command: `python names_challenge.py`
    print(names_func(["one", "two", "three", "four", "five"], 2))
