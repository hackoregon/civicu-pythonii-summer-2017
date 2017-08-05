# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 
import csv
import collections


def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        my_reader = csv.reader(coffee_csv)
        #calling next will return the next row in the file 
        #which is often the row of headers
        #header = next(my_reader)
        for row in my_reader:
            print(row)
    return

def csv_airports():
    with open("airports.csv") as airports_csv:
        airports_reader = csv.reader(airports_csv)
        
        header = next(airports_reader)
        
        for row in airports_reader:
            print(row)
            
    return
                           
def csv_airports_from_country(country):
    with open("airports.csv") as airports_csv:
        airports_reader = csv.reader(airports_csv)
        
        header = next(airports_reader)
        
        for row in airports_reader:
            if str(row[3]) == country:
                print(row)
                
    return

        
        
        
        
#csv_coffee()
#csv_airports()
csv_airports_from_country('Germany')