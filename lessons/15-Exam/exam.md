# Exam

## Submitting Your Answers

Submit your answers to all questions to my exam app that I created from the labeler app pattern.

## Code Challenge

All of your code for the three code challenges should be written in a single python module (.py file) called `civiu_advanced_python_exam.py`.
As you'll see later, this module will also contain your answers to the multiple choice questions.
This file should be placed in the directory `student-work/your_name/exam/`, commited and pushed to your repository on github and then PRed to our class repository at `github.com/hackoregon/civicu-pythonii-summer-2017`.


### Challenge 1

Write a function called `read_exam` that takes as its only input a string with the URL or a file system path to a *.CSV file.
The default value for this single argument to your function should be "../../../lessons/shared-resources", but it doesn't have to work with this path to get full credit.

- If your function only works for a local path you get full credit.
- If it only works for a URL you get full credit plus a bonus point.
- If it works for both a local file path **and** a URL you get 2 bonus points.

Your fu

global variables called "QUESTIONS" that contains the multiple choice questions stored in the CSV file "exam.csv" in the lessons/shared-resources/ folder within the github repository for this class, "ANSWERS", and "SUBMISSIONS" that each contain:

- `QUESTIONS`: The question numbers.
- `ANSWERS`: The answer letters corresponding to each question number.
- `SUBMISSIONS`: The A list of dictionionaries, each dictionary with 2 keys ('question' and 'answer') and 2 values (one for each of those keys)

**HINT:** `zip` and `zip(*...)` will make things easier, but aren't required.

All 3 lists should be exactly 10 long, so write a doctest within the module's docstring that tests this.


### Questions

#### 1. 
 that contains a list of dictionaries with answers to the 10 multiple-choice questions.
Add a doctest to the docstring for the file that tests that the length of your `ANSWERS` list is 
Each question/answer pair should be 

