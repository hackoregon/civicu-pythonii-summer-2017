# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:07:31 2017

@author: Dennis
"""

import requests
import json


def pretty_print(json_obj):
    """Helper function to pretty print json"""
    return json.dumps(json_obj, indent=4)

# making a simple `GET` request to get all the SWAPI film data
response = requests.get("http://swapi.co/api/films/")

# when we run the line above, we end up with a response object that has 
# certain attributes we can access to gain information about the response object

print(response.status_code) # will print out the status code of the request, hopefully 200

print(response.headers) # will print out any header information in the request

response = requests.get("http://swapi.co/api/films/")

# by calling .json() on our response we get a Python dictionary of all the data that the server sent us
response_dict = response.json()

# try printing this out and see how it looks 
print(response_dict)


