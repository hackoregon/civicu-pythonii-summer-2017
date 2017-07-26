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

# open_airports()

#lat1, lat2, long1, long2
def get_route_distance():
    #Make latitude Dictionary
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_header = next(airport_reader)
        latitudes = {row[0]:row[6] for row in airport_reader}
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        longitudes = {row[0]:row[7] for row in airport_reader}
    with open("routes.csv") as routes_csv:
        route_reader = csv.reader(routes_csv)
        route_header = next(route_reader)
        no_id = 0
        errors = []
        for row in route_reader:
            from_air = row[3]
            to_air = row[5]
            #Get origin lat, longs
            try:
                from_lat, from_long = latitudes[from_air], longitudes[from_air]
                print(from_lat, from_long)
            except KeyError:
                no_id += 1
                if from_air not in errors:
                    errors.append(from_air)
            #Get destination lat, longs
            try:
                to_lat, to_long = latitudes[to_air], longitudes[to_air]
                print(to_lat, to_long)
            except KeyError:
                no_id += 1
                if to_air not in errors:
                    errors.append(from_air)
            route_distance = distance(from_lat, from_long, to_lat, to_long)
            print(route_distance)
            # new_row = [from_air, lat1, long1, to_air, lat2, long2, distance]
            # with open("combined_file.csv", "a") as combined:
            #     combined.write()

        print("Records that don't match:", str(no_id))
        print("Errors: ",errors)

get_route_distance()
