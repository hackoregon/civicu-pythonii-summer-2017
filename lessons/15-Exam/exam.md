# Exam

## Submitting Your Answers

Submit your answers to all questions to my exam app that I created from the labeler app pattern.

## Code Challenge

All of your code for the three code challenges should be written in a single python module (.py file) called `exam.py`.
As you'll see later, this module will also contain your answers to the multiple choice questions.
This file should be placed in the directory `student-work/your_name/exam/`, commited and pushed to your repository on github and then PRed to our class repository at `github.com/hackoregon/civicu-pythonii-summer-2017`.

### Code Challenge 1

Download the exam.csv file from here: `https://raw.githubusercontent.com/hackoregon/civicu-pythonii-summer-2017/ceasar/lessons/shared-resources/exam.csv`

Write a function called `read_exam()` that takes as its only input a string with the URL or a file system path to a *.CSV file.
The default value for this single argument to your function should be a relative path from your the path containing your `exam.py` script to the exam.csv file.
For example `'../../../lessons/shared-resources/exam.csv'` might work if you put your exam.py file in `student-work/your_name/exam/` and you've put your exam.csv file in `lessons/shared-resources`.
This is the folder where the file exists on the `ceasar` branch of the hackoregon repo for this class.

- If your function works for any local path to a csv file you get full credit.
- If it only works for a URL you get full credit plus a bonus point.
- If it works for both a local file path **and** a URL you get 2 bonus points.
- If you have a useful doctest for the function that passes you get an additional bonus point

Your `read_exam()` function should return 3 lists in a 3-tuple of lists.

- First object in the tuple: `list` of the question numbers from the exam.CSV file
- Second object in the tuple: `list` of the question text strings from the exam.CSV file
- Third object in the tuple: `list` of the incorrect answers to the questions from the exam.CSV file

## Code Challenge 2

If I import your `exam` module it should contain 5 global variables:

- `QUESTIONS`
- `ANSWERS`
- `QUESTION_TEXTS`
- `MY_ANSWERS`
- `MY_ANSWERS_JS`

#### `QUESTIONS`, `ANSWERS`, and `QUESTION_TEXTS`

The variables `QUESTIONS`, `ANSWERS`, and `QUESTION_TEXTS` should contain `list` objects with the 3 lists returned by the `read_exam()` function in **Challenge 1**.
If you are unable to get `read_exam()` working, you are allowed create these lists "by any means necessary," like typing or copying and pasting text and code from the CSV file to create these lists.

#### `MY_ANSWERS` 

The global variable `MY_ANSWERS` should contain a list of your answers to all the questions in the CSV file.
Each element (object) of the list should be of type `str` and contain a sequence of letters A-H for each of the possible answers.
Many of the latter questions contain multiple answers so you will have more than one letter in many of these strings.
You'll need to correct the answers in the CSV file, because I will grade these answers.

#### `MY_ANSWERS_JS` 

`MY_ANSWERS_JS` should contain a string which is the `json` "fixture" of the data in two of these 3 lists as if the CSV file were stored in a Django Database.
If I run `json.loads(exam.MY_ANSWERS_JS)` it should return a list of 11 dictionaries that looks like this:

```python
[
{ 
  'id': 0,
  'my_answer': 'B'
},
{ 
  'id': 1,
  'my_answer': 'D'
},
...
{
  'id': 10,
  'my_answer': 'ABCDEFG'
```

**HINT:** `zip` and `zip(*...)` will make things easier, but aren't required.

All 4 lists should be exactly 11 long.
The json string will of, of-course, be much longer.

- Bonus: Write a doctest for your module that verifies the length of the 4 lists.
- Bonus: Populate these variables "programatically" using `globals()` within a function called `setup()` that is run in the global context of your module.


### Code Challenge 3

Write a "unittest" that checks that each of the answers in your answer `exam.MY_ANSWERS` are what you intended.

