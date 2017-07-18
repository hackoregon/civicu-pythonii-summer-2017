# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving
# your work.


import csv
import collections
# import geo_distance

def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        my_reader = csv.reader(coffee_csv)

        # calling next will reutrn the next row in the file which is often the row of headers
        # header = next(my_reader)

        for row in my_reader:
            # print(row)
            pass

        [print(row) for row in my_reader if row[0] == 'Flat White']

def csv_airport():
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        for row in csv.reader(airports_csv):
            if row[3] == 'England':
                print(row[1])

csv_coffee()
csv_airport()
