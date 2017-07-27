# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 

import csv

f = open("coffee.csv")
for row in csv.reader(f):
    print(row)

#use this file to print all of the airport names for a particular country (say, Australia or Russia)?
def csv_airport():
    with open("airports.csv") as airports_csv:
        airport_reader =csv.reader(airports_csv)
        airport_header = next(airport_reader)
        print(airport_headers)

def counts airpirt in country

def calc airport distances

