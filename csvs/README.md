## Basics of reading and writing to CSVs

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

We'll get more familiar with csvs by using an exercise provided by `OpenTechSchool`. You can find the link to the exercise [here](http://opentechschool.github.io/python-data-intro/core/csv.html). Before starting this exercise please read the notes below about the changes/modifications that have been made to suit the needs of our class.

## Explanation of challenges in the `OpenTechSchool` exercise
In the sections below we'll walk through each of the pieces of the exercise linked above. Note that we're not going to be working on the last section of the provided challenge where we're asked to plot the results of the distance calculation.

### Coffee csv challenge
In this exercise our task was to open a csv and loop through the rows it contained. This is useful because it is the basic pattern we will follow anytime that we want to access data that is being stored in a csv. 
```Python
def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        my_reader = csv.reader(coffee_csv)

        for row in my_reader:
            print(row)
```
Notice how we define a reader object that then lets us loop through each row that is inside of the `coffee.csv` file. Remember that when looping through the rows in a csv the values in each row will be given to you as a list of strings.

### Reading airport data challenge 
In this part of the challenge we are looking at the `airports.csv` file and are tasked with printing out only the rows for airports that are in a specific country. You can pick any country you like for this challenge. 

```Python
def csv_airport():
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_headers = next(airport_reader)
        print(airport_headers)

        for row in airport_reader:
            if row[3] == "Canada":
                print(row)
```
In the solution above we're opening a csv.reader object so we're then able to loop through the rows contained in the `airport.csv`.

Notice how we call the `next()` function with the `airport_reader` as an argument in order to get the first row from the csv. 
In this case it is the header row that contains information about the contents in each column. See header row contents below.
```Python
# header row contents
['ID', ' Airport-Name', ' City', ' Country', ' IATA', ' ICAO', ' Latitude', ' Longitude', ' Altitude', ' Timezone', ' DST', ' Tz-Type', ' Source']
```
Just like all rows that we get back from the csv reader the header row is a list of strings. The header row let us know what the values in each column of the csv mean. For this challenge we're looking for the country that an airport is from so we know that we need to check the value at the 3rd index when we're looping through each row in the csv.

We then loop through each row using a for loop and check to see if the value in the 3rd index is equal to `"Canada"`. If the airport is from Canada we then print out the row.

As an extra challenge try to change this function so that you can pass in an argument that is a country's name and then only print the rows that have an airport from that country.


### Calculating the distances between two airports
In this part of the challenge we were asked to calculate the distance for all of the airline routes in the `routes.csv`. In order to solve this part of the challenge we need to combine data that we have in two different files to get the correct information to perform this task. 

We are given a `geo_distance` function seen below to help us with this calculation.
```Python
# Using the Haversine formula for geographic Great Circle Distance
# As per https://en.wikipedia.org/wiki/Haversine_formula

from math import cos,radians,sin,pow,asin,sqrt

def distance(lat1, long1, lat2, long2):
    radius = 6371 # radius of the earth in km, roughly https://en.wikipedia.org/wiki/Earth_radius

    # Lat,long are in degrees but we need radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    dlat = lat2-lat1
    dlon = long2-long1

    a = pow(sin(dlat/2),2) + cos(lat1)*cos(lat2)*pow(sin(dlon/2),2)
    distance = 2 * radius * asin(sqrt(a))

    return distance
```
It's not necessary to understand the equation being used in this function in order for us to be able to use it to calculate the distance between two points. If we look at the function we can see that it takes four arguments, two pairs of lat/long coordinates.

In order to solve this challenge we need to pass in the lat/long coordinates for each set of airports found in the rows of the `routes.csv`. 

The problem is all of our lat/long information is stored in the `airports.csv` and is only stored once per airport. This is a common pattern when storing information about items that relate to one another. In this case each individual airport could have potentially dozens of routes (rows in the `routes.csv`) leaving to and from it daily. If we were to store the lat/long for each airport in every row in the `routes.csv` we would be writing down a ton of repetitive information and would make the file much larger than it needs to be. Instead the csv is setup to use the unique id for each airport when they need to describe any relationship between airports. Doing this lets us model the relationship between two airports without having to write down a bunch of extra information about each airport on every row of the `routes.csv`.

If we want to calculate the distance between two airports it's up to us to look up the pieces of information we need from the `airport.csv` so we can then use that information when we're looping through the `routes.csv`.

In the examples below we'll walk through the process of building up the lat/long information we need.
```Python
def calc_airport_distances():
    # define two empty dicts that will hold our lat/long info
    airport_lats = {}
    airport_longs = {}

    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_headers = next(airport_reader)

        for row in airport_reader:
            airport_lats[row[0]] = float(row[6])
            airport_longs[row[0]] = float(row[7])
```
In the code above we define two empty dicts and then loop through each row in the `airports.csv` grabbing the `id` at the 0th index and then the lat or long depending on which dictionary we're adding the information to. Remember that the `id` for an airport is the same in both the `airports.csv` and the `routes.csv`


By doing this we're building a lookup dictionary that we can use later when we loop through the `routes.csv` and need the lat/long for each airport. Notice that we're also converting the `string` values to `float` with the lat/longs so that we can use them in the `geo_distance` function later.

Now that we have two dictionaries that contain the lat and long for each airport we're ready to loop through the `routes.csv`. 

In order to know which indexes we need values from in the `routes.csv` it's helpful to look at the headers. See below

```Python
# route.csv headers
['Airline', ' Airline-ID', ' Source-airport', ' Source-airport-ID', ' Destination-airport', ' Destination-airport-ID', ' Codeshare', ' Stops', ' Equipment']
```

Looking at the headers we can see that we want to lookup the `Source-airport-ID` (the 3rd index) and the `Destination-airport-ID` (the 5th index). The ids in these positions will match the ids from the airports in the `airports.csv` and will give us a way to look up the lat/long information we need using the dictionaries we created above.

Below I've included the code that opens the `routes.csv`. Notice how we do this in the same function where we're building out lookup dictionaries. We could have these as two separate functions but it makes it easier to keep everything in one place for the moment.


```Python
def calc_airport_distances():
    # define two empty dicts that will hold our lat/long info
    airport_lats = {}
    airport_longs = {}

    with open("airports.csv") as airports_csv:
        # setup reader and remove header
        airport_reader = csv.reader(airports_csv)
        airport_headers = next(airport_reader)

        for row in airport_reader:
            airport_lats[row[0]] = float(row[6])
            airport_longs[row[0]] = float(row[7])
            
    # now that we have lookup dicts for lat/long loop through the routes 
    with open("routes.csv") as routes_csv:
        route_reader = csv.reader(routes_csv)
        route_headers = next(route_reader)

        for row in route_reader:
            source_id = row[3]
            dest_id = row[5]

            # check to see if the ids for both airports are in the lookup dicts
            if source_id in airport_lats and dest_id in airport_lats:
                # use the lat/long dicts to get the coordinate info for each airport
                source_lat = airport_lats[source_id]
                source_long = airport_longs[source_id]
                dest_lat = airport_lats[dest_id]
                dest_long = airport_longs[dest_id]
                
                # make a variable that captures the output from the geo_distance function
                km_dist = geo_distance.distance(source_lat,
                                                source_long,
                                                dest_lat,
                                                dest_lat)
```
At this point if you run the code above it will build the lookup dicts we need for the lat/long values by opening the `airports.csv`. Then it will open the `routes.csv` pull off the headers and loop through each row grabbing the source and destination airport ids from each set of airports. It then checks that the source and destination airport ids are in the lat/long dicts and if they are it grabs the lat/long pairs for each airport. With these coordinate pairs we're then able to pass them into the `geo_distance` function and grab the distance between the airports for each row in the `routes.csv`. 

With the code above we're calculating the distance value but not saving it anywhere, in each loop we calculate the kilometer distance between the two airports but then throw that value away. If we wanted to save this calculation so that we could use it later on in a different program we could write it to a new csv. Look at the code below and see how we're able to open a csv to write our information to while we're looping through the `routes.csv`

```Python
def calc_airport_distances():
    # define two empty dicts that will hold our lat/long info
    airport_lats = {}
    airport_longs = {}

    with open("airports.csv") as airports_csv:
        # setup reader and remove header
        airport_reader = csv.reader(airports_csv)
        airport_headers = next(airport_reader)

        for row in airport_reader:
            airport_lats[row[0]] = float(row[6])
            airport_longs[row[0]] = float(row[7])
            
    # now that we have lookup dicts for lat/long loop through the routes 
    with open("routes.csv") as routes_csv:
        route_reader = csv.reader(routes_csv)
        route_headers = next(route_reader)

        for row in route_reader:
            source_id = row[3]
            dest_id = row[5]

            # check to see if the ids for both airports are in the lookup dicts
            if source_id in airport_lats and dest_id in airport_lats:
                # use the lat/long dicts to get the coordinate info for each airport
                source_lat = airport_lats[source_id]
                source_long = airport_longs[source_id]
                dest_lat = airport_lats[dest_id]
                dest_long = airport_longs[dest_id]
                
                # make a variable that captures the output from the geo_distance function
                km_dist = geo_distance.distance(source_lat,
                                                source_long,
                                                dest_lat,
                                                dest_lat)
                
                # open a csv file that we want to append information to and write a row
                with open("dist_info.csv", "a") as dist_info:
                    dist_info_writer = csv.writer(dist_info)
                    dist_info_writer.writerow([source_id, dest_id, km_dist])
```
While the code above is not the most efficient way to write to the new `dist_info.csv` because we're repeatedly opening and closing it every time we loop through a row of the `routes.csv` it gives us a quick example of how you can save information to a file. If you run the code above you'll see a new `dist_info.csv` file created in the directory you're in. By using the `a` flag when we open the file we're saying that we want to append information to it and not overwrite what is already there. If you were to use `w` instead of `a` you would end up with only one row in your newly created file because it would erase the file every time we opened it inside the loop.

### Ideas for further challenges
Now that we have seen a rough way to solve this problem I would like everyone to try to modify the code above in some way. Below you'll find ideas of possible side projects. These aren't required but would be a useful way to get extra practice. 
* Try to write more information than just the `source_id`, `dest_id`, and `km_dist` to the final csv. (remember that when using the `a` flag no information is erased, so multiple runs of the function above will keep adding rows) 
* Try to rework how the code is organized so instead of having one large function that does everything, break the steps needed to solve this problem into smaller pieces contained in separate functions. 
* Find other interesting csv data that is openly available and see if you can pull out the pieces that interest you and write them to a new csv using the techniques described above.

### Useful ways to inspect files
There are a few useful commands if you're on a linux/unix os that can help you inspect the csv files you're creating. The commands are listed below with a brief description of what they do. [Link to stackoverflow question about using tail command on windows](https://stackoverflow.com/questions/1295068/windows-equivalent-of-the-tail-command)

* `tail <file_name>` - This will show you the last 10 lines of a file in the terminal
* `head <file_name>` - This will show you the first 10 lines of a file in the terminal
    * with both commands above you can pass additional flags to them that cause different outputs. One useful flag is the `-f` flag. This flag will let you follow what is happening to the file so if you have a long running write you can visually check that the file is getting written to. [Link to other flags](https://www.linux.com/blog/14-tail-and-head-commands-linuxunix)
* `wc -l *` - If you run this command in a directory with your csv files if will count the lines in each one. It's a useful way to spot check files and make sure that you go the correct number of rows you were expecting.

### Using `try` and `except`
In class we talked briefly about how it can be useful to use try and except blocks to catch errors and to make note of information that might be off in different parts of your csv. No try and except blocks were included in the code above in order to keep the focus on manipulating csvs. However, using try and except can be a useful troubleshooting tool when trying to convert values. In the code snippet below you can see a bit of sudo code that outlines one way you could use a try and except block to keep track of errors when trying to convert a value in a csv to an `int`.

```Python
bad_val_dict = collections.defaultdict(int)
try:
    fake_val = int(row[0])
except ValueError:
    bad_val_dict[row[0]] += 1
```
What this does is allow us to catch values that weren't able to be converted to ints and then store a count of those values in a dict that we can then inspect later. This can be useful as a way to get a quick count of the bad values that may be present in a csv. 

There was also a question about printing the exact error and traceback that caused an error when using a try and except block. This is done using the `traceback` module and an example can be seen below. 

```Python
import traceback

try:
    # will cause zero division error
    x = 5 / 0
except:
    # this will print the exact error that occurred
    traceback.print_exc()
```


