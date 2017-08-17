# Using the requests library

Python's requests library gives us an easy way to make requests and then access the results of those requests in our code. What we will be working through today is one of the basic building blocks of making a scraper that can grab data you might be interested in from the web. The requests library will allow you to send HTTP requests using Python. It also gives us an easy way to add headers, form data, and parameters to the requests that we send. 

### Installing and importing requests
The requests library needs to be installed and can be installed easily using pip. Run `pip install requests` in a terminal and you should be good to go. Then you just import the module like any other at the top of your file. 

### Using the Star Wars API (SWAPI)
The [Star Wars API](http://swapi.co/documentation) is what we will be using today during our group challenge to get familiar with making requests and parsing JSON. This API is ideal for this purpose because it doesn't require user authentication and will let us make up to 10,000 requests per day without being rate limited. Below you'll find the basic building blocks for making `GET` requests.

#### Example `GET` request
```Python
import requests

# making a simple `GET` request to get all the SWAPI film data
response = requests.get("http://swapi.co/api/films/")

# when we run the line above, we end up with a response object that has 
# certain attributes we can access to gain information about the response object

print(response.status_code) # will print out the status code of the request, hopefully 200

print(response.headers) # will print out any header information in the request
```

#### Requests built in JSON decoder

The requests library has a built in JSON decoder that lets us decode the JSON object sent in the body of a response. 
```Python
response = requests.get("http://swapi.co/api/films/")

# by calling .json() on our response we get a Python dictionary of all the data that the server sent us
response_dict = response.json()

# try printing this out and see how it looks 
print(response_dict)
```

#### Pretty printing JSON
In the code snippet below there is a little helper function that we can call with any of our decoded JSON objects as an argument and it will print them out in a better format. Feel free to just use the `json.dumps(your_json_obj, indent=4)` pattern on its own as well.
```Python
import json


def pretty_print(json_obj):
    """Helper function to pretty print json"""
    return json.dumps(json_obj, indent=4)
```

### Other pieces of the Requests library

The requests library lets you do a lot more than just make `GET` requests but for the SWAPI that is mainly how we will use it. To see more information on the different things you can do with requests, the links below will lead you to the documentation and a good tutorial.

* [requests library docs](http://docs.python-requests.org/en/master/)
* [quickstart tutorial](http://docs.python-requests.org/en/master/user/quickstart/) - Has a bunch of good information on making more complicated requests.

## SWAPI class example
For tonight's class example we're going to practice making `GET` requests to the Star Wars API, parsing the response we recieve, and then writing the information we find to a csv. Working through this process together should help everyone get a good handle on the basics of making requests and accessing information from their responses. [SWAPI docs](http://swapi.co/documentation)

We'll now work together to complete the following steps:
* Make a `GET` request to get information about the planet with the id of 1
* Loop through the `residents` attribute in planet 1's response making `GET` calls to get the name of each resident
* Write the planet name, planet url, and all residents names to a line in a csv

In the examples below we'll print out different pieces of information as we go so we're able to see the process. Follow along by copying and pasting this code into your editor. If you are copying and pasting make sure to add each Python example one after the other and make sure you're calling each function. 

#### Making a request about planet 1
```Python
import csv
import json
import requests


def pretty_print(json_obj):
    """Helper function to pretty print json"""
    return json.dumps(json_obj, indent=4)

def planet_request():
    """
    This will make a request and then print out all the information
    about a planet including the headers and status for the response
    """
    planet1 = "http://swapi.co/api/planets/1/"
    p1_req = requests.get(planet1)

    # print out the meta info about our request
    print(p1_req.status_code)
    print(p1_req.headers)

    # printing out the body of the request
    print(pretty_print(p1_req.json()))
  
  
# make sure to call the function
planet_request()
```

#### Inspecting planet 1's JSON response
This is the output you should see if you run the code above.
```json
{
    "diameter": "10465",
    "population": "200000",
    "rotation_period": "23",
    "gravity": "1 standard",
    "terrain": "desert",
    "url": "http://swapi.co/api/planets/1/",
    "created": "2014-12-09T13:50:49.641000Z",
    "residents": [
        "http://swapi.co/api/people/1/",
        "http://swapi.co/api/people/2/",
        "http://swapi.co/api/people/4/",
        "http://swapi.co/api/people/6/",
        "http://swapi.co/api/people/7/",
        "http://swapi.co/api/people/8/",
        "http://swapi.co/api/people/9/",
        "http://swapi.co/api/people/11/",
        "http://swapi.co/api/people/43/",
        "http://swapi.co/api/people/62/"
    ],
    "name": "Tatooine",
    "films": [
        "http://swapi.co/api/films/5/",
        "http://swapi.co/api/films/4/",
        "http://swapi.co/api/films/6/",
        "http://swapi.co/api/films/3/",
        "http://swapi.co/api/films/1/"
    ],
    "climate": "arid",
    "edited": "2014-12-21T20:48:04.175778Z",
    "surface_water": "1",
    "orbital_period": "304"
}
```

Looking at the output you'll notice that there is an attribute called `residents` which is a list of urls that point to all of the different characters that lived on Tatooine in the Star Wars movies. If we wanted to get the names of all the residents that lived on this planet we would need to make requests to all those urls and pull the name attribute out of each.

Below we make a new function that gets the planet's info and the names of the residents.

```Python
def get_all_residents_of_planet_1():
    """Get the names of all residents on planet 1 and write them as a row to a csv"""

    planet1 = "http://swapi.co/api/planets/1/"
    p1_res = requests.get(planet1).json()
    print(pretty_print(p1_res))

    # grab the planet name and the planet url
    p1_name = p1_res["name"]
    p1_url = p1_res["url"]

    # make an output list that will hold our planet name, url, and list of residents
    output_list = [p1_name, p1_url]

    # this grabs the list of resident urls from response
    res_urls = p1_res["residents"]

    for resident_url in res_urls:
        resident_res = requests.get(resident_url).json()
       
        # uncomment this if you want to see what the response for each resident looks like
        # print(pretty_print(resident_res))
       
        # these lines get the resident's name
        resident_name = resident_res["name"]
        output_list.append(res_name)

    print(output_list)
    
    
get_all_residents_of_planet_1()
```

The function above shows how we can combine both pieces of making the initial request for the planet information and then looping through the urls contained in the `residents` attribute, making an additional `GET` request for each resident url. Also notice how we're appending each resident's name to the ouput list we created earlier in the function that already contained the planet name and planet url.


#### Writing the information we gathered to a csv
Now for the final bit we can add the code below inside the __get_all_residents_of_planet_1__ function above to write the output list we created to a `planet_pop.csv` file. Notice how we're using the `a` flag to open the file. This will cause the writer to append to what already exists in the file and won't overwrite already existing rows.

```Python
# add this piece inside the function above to write the output row to a csv
    with open("planet_pop.csv", "a") as planet_pop:
        planet_writer = csv.writer(planet_pop)
        planet_writer.writerow(output_list)
```

## Small group challenges
In your small groups I'd like you to spend the rest of the class playing with the Star Wars API and getting familiar with making `GET` requests and pulling information out of the responses. Below are a list of possible tasks, do your best to complete what you can but don't feel like you need to finish them all. Just make sure you have a good sense of what's going on.

* Refactor the code in our last function above so that it uses a seperate function to make the requests that grab a resident's name. It's often useful to break functions into little pieces that only do one thing each. That way they're more resusable and are easier to test.
* Rewrite our final function to be able to loop through all of the planets instead of just the first one writing the information for each planet as a row in the `planet_pop.csv` 
* Find another endpoint in the SWAPI that you want to pull information from and write a set of functions to make the requests to gather that information. 

