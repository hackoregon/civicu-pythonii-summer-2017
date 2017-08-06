# Group challenge

This will be a three part challenge that everyone will be working in small groups of three to solve. Please talk with your group about what you're doing and help each other if you get stuck along the way. Below you'll find an outline of the problem requirements. 

## Challenge requirements
* make a group of three classes that model students and a teacher in a usual classroom. You should use a base class for the shared characteristics and between both Student and Teacher classes. 

* Shared attributes and methods for both classes:
    * Shared attributes: first_name, last_name, email
    * Shared methods: ask_a_question
    
* Student attributes and methods that need to be added in addition to those shared above:
    * Student attributes: books_dict - create a dictionary that contains the books a student owns.
    * Student methods: 
        * add_book - this method will add a book to the student's books_dict.
        * remove_book - this method will remove a book from the student's books_dict.
        * show_books - this method will print out all of the books a student owns.
        
* Teacher attributes and methods that need to be added in addition to those shared above:
    * Teacher attributes: student_list - create a list of student names 
    * Teacher methods:
        * shuffle_class - this method will take all of the students in the student list and put them in work groups (see names_challenge problem below)
        
### Names challenge function 

The goal of this challenge is to create a function that will take a list of 
names and a bin size and then shuffle those names and return them in a 
list of lists where the length of the inner lists match the bin size. 

For example calling the function with a list of names and size 2 should return 
a list of lists where each inner list has 2 random names. If the the number
of names provided doesn't divide evenly into the bin size and only one name is 
remaining add that name to another inner list. 

Also note that there is a test file called `names_challenge_test.py` that has a number of tests which will help give feedback when solving this part of the problem. 

Once you have completed this part of the challenge try to add the function you created as a method on the Teacher class above and have it run on the `student_list` attribute.
