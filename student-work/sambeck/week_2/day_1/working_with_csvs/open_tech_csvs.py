# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 

import csv


def print_airports(country):
    with open('airports.csv') as air:
        airports = csv.reader(air)
        header = next(airports)
        # print(header)
        count = 0
        for row in airports:
            if row[3] == country:
                print(row)
                count += 1
        print(count)
