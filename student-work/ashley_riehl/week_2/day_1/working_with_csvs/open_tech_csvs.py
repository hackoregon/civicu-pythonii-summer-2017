# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving
# your work.

import csv

def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        my_reader = csv.reader(coffee_csv)

        # header = next(my_reader)

        for row in my_reader:
            print(row)
        # water = [row[0] for row in my_reader if row[1] == "No"]
        # print(water)

# csv_coffee()

def open_airports():
    with open("airports.csv") as airports_csv:
        my_reader = csv.reader(airports_csv)
        header = next(my_reader)
        for row in my_reader:
            if row[3] == 'Latvia':
                print(row)

open_airports()
#dict of airports and lat, long

def get_route_distance()
    #Make latitude Dictionary
    with open("")
    latitudes = {id:lat for }
    #Make longitude Dictionary
