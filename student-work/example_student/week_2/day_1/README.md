# List comprehensions
List comprehensions offer a convenient way to create lists based on existing lists or any other iterable. List comprehensions give us a different way to create lists that can make code easier to read and take up less space.

## List comprehension syntax

```Python
list_variable = [x for x in iterable]
```

A list comprehension is basically like a in-line for loop that lets us create a new list of items from any existing iterable. In the syntax example shown above the first `x` represents what is being added to the new list you're creating. The following `for x in iterable` part is the same syntax that you're familiar with in regualr for loops. What the example above does is take any item that came out of the iterable and place it in a list.

## Consider the examples below

```Python 
bicycle_sent = 'a blue bicycle'

# get a list of all letters with a for loop
bicycle_letters = []
for letter in bicycle_sent:
    bicycle_letters.append(letter)
    
# get all letters with a list comp
bicycle_letters = [letter for letter in bicycle_sent]
```

### Using conditionals

```Python
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

# make a list of all fish with a for loop
fish_list = []
for fish in fish_tuple:
    if fish != 'octopus':
        fish_list.append(fish)
        
# make a list of all fish using a list comp
fish_list = [fish for fish in fish_tuple if fish != 'octopus']

# nesting conditionals
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
# number_list = [0, 15, 30, 45, 60, 75, 90]
```

### Modifying values
Notice how you're able to modify values as you add new items to the list you're creating
```Python
list_nums = [1, 2, 3]

# multiply each nummber in a list by 3
times_three = [(num * 3) for num in list_nums]
```

### Set comprehensions

```Python

word = 'mississippi'


# building a set using a for loop
unique_letters = set()
for letter in word:
    unique_letters.add(letter)
    
# a set comprehension
unique_letters = {letter for letter in word}
```

### Dictionary comprehensions
```Python
my_dict = {"a": 1, "b": 2, "c": 3}

# using a for loop
flipped_dict = {}
for key, value in my_dict.items():
    flipped_dict[value] = key

# using a dict comp
flipped_dict = {value: key for key, value in my_dict.items()} 
```

## Exercism exercise
Please work with the person next to you to solve the following Exercism problem. Try to solve this exercise using some type of comprehension in your answer.
In order to get this exercise run the following command in your terminal: `exercism fetch python isogram`. This will download the challenge to the exercism folder in your home directory. When you're finished run `exercism submit <path_to_your_solution>isogram.py`


-----------------------------------------------------------
# Context managers

The most common and important use of context managers is to properly manage resources. This usually means the opening and closing of files that you might want to write data to. Context managers give us an easy way to make sure that files get closed when we're done using them. 

*File descriptors* - every time you open a file, the operating system assigns an integer to the file that gives you a way to reference the open file that you can then pass between processes. If we try to open too many files, the operating system will throw an error.

### Opening too many files causes an error
```Python
# This won't work because we're not closing any of the files we're opening
files = []
for x in range(100000):
    files.append(open('foo.txt', 'w'))
```

### Context managers vs. just calling close()
```Python
# opening a file and then calling .close()
f = open('foo.txt', 'w')
f.close()

# opening a file using the `with` context manager
with open('foo.txt', 'w') as foo_file:
    # do something with foo, and the file will automatically close
```

You can use `with` to call anything that returns a context manager. One way an object can be considered a context manager is if it has both `__enter__` and `__exit__` methods. Then calling that object using `with` will cause the `__enter__` method to be executed at the start of the with block and then the `__exit__` mehtod will be called when the program exits the `with` block. See example below.

```Python
class MyContext():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with MyContext('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)
```

We will now move on to a section about manipulating csv files. Please move into the `working_with_csvs` directory and see the README file there. 

