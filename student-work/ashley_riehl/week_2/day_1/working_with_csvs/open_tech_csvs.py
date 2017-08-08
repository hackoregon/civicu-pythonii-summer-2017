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

def get_route_distance():
    #Make latitude dictionary
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_header = next(airport_reader)
        latitudes = {row[0]:row[6] for row in airport_reader}

    #Make longitudes dictionary
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        longitudes = {row[0]:row[7] for row in airport_reader}

    #Lookup coordinates to routes
    with open("routes.csv") as routes_csv:
        route_reader = csv.reader(routes_csv)
        route_header = next(route_reader)

        #Keep track of lookup errors
        no_id = 0
        errors = []

        for row in route_reader:
            from_air = row[3]
            to_air = row[5]

            #Get origin lat, longs
            try:
                from_lat, from_long = float(latitudes[from_air]), float(longitudes[from_air])
            except KeyError:
                no_id += 1
                if from_air not in errors:
                    errors.append(from_air)

            #Get destination lat, longs
            try:
                to_lat, to_long = float(latitudes[to_air]), float(longitudes[to_air])
            except KeyError:
                no_id += 1
                if to_air not in errors:
                    errors.append(from_air)

            #Calculate route distance
            route_distance = distance(from_lat, from_long, to_lat, to_long)

            #Save to new file
            new_row = [from_air, from_lat, from_long, to_air, to_lat, to_long, route_distance]
            with open("combined_file.csv", "a") as combined:
                combined_writer = csv.writer(combined)
                combined_writer.writerow(new_row)

        #Print any lookup errors
        print("Records that don't match:", str(no_id))
        print("Errors: ",errors)

get_route_distance()
