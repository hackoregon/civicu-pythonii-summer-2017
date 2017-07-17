## Basics of reading an writing to CSVs

* [links to CSV docs](https://docs.python.org/3/library/csv.html)
* [open() func docs - section on available flags](https://docs.python.org/3/library/functions.html#open)

Today we'll be focusing mainly on using the csv `reader` and `writer`. These tools help us when needing to parse csv files and will serve as a quick and easy way to store data we might want to collect. Below you'll find examples of using a csv reader and writer.

### CSV reader and writer
```Python
import csv

# reader example
with open("foo.csv") as foo: 
    foo_reader = csv.reader(foo)
    
    # this is how you can grab the first header row out of a csv
    header_row = next(foo_reader)
    
    for row in foo_reader:
        print(row)
   
    
# writer example 
with open("foo_write.csv", "w") as foo:
    foo_writer = csv.writer(foo)
    foo_writer.writerow(("col val 1", "col val 2", "col val 3", "col val 4"))
    
```

We'll get more familiar with csvs by using an exercise provided by `OpenTechSchool`. You can find the link to the exercise [here](http://opentechschool.github.io/python-data-intro/core/csv.html). Before starting this exerices please read the notes below about the changes/modifications that have been made to suit the needs of our class.

### Notes about OpenTechSchool exercise
* The csv files for these exercises have been added to the `shared-resources` directory in the top level of the class repo, please use the files there when working on these challenges
* Header information has been added to each csv file (except the coffee one), remember to pull the header row out of your csv before looping through the information cointained inside (see example in code snippet above) 
* As common with most csv files, there is some data included in these files that might not be able to be converted using `int()` or `float()` easily. If you run into this problem, consider using `try` and `except` as a quick work around to get to an end solution

* Other notes:
    * There is a file called `geo_distance` in your individual student work directory. This is where the function to calculate the distance between two airports is coming from 
    * Please make sure that you're opening all files using the `with open()` pattern that is shown above
 
