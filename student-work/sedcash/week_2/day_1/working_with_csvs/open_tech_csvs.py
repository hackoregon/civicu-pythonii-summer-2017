# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving
# your work.

import csv
from geo_distance import distance



def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        coffee_reader = csv.reader(coffee_csv)
        for row in coffee_reader:
            print(row)
    return

def csv_airport(word):
    with open("airports.csv") as airport_csv:
        airports_reader = csv.reader(airport_csv)
        airports_header = next(airports_reader)
        return [airport[1] for airport in airports_reader if airport[3] == word]

def calulate_airport_distance(id1, id2):
    with open("airports.csv") as airport_csv:
        airports_reader = csv.reader(airport_csv)
        airports_header = next(airports_reader)
        airport_latitude_list = {}
        airport_longitude_list = {}
        for airport in airports_reader:
            airport_latitude_list[int(airport[0])] = float(airport[6])
            airport_longitude_list[int(airport[0])] = float(airport[7])
    with open("route.csv") as route_csv:
        route_reader = csv.reader(route_csv)
        route_header = next(route_reader)
        distance(airport_latitude_list[id1],airport_longitude_list[id1], airport_latitude_list[id2], airport_longitude_list[id2])


