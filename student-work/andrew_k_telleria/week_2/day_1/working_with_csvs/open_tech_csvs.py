# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving
# your work.


import csv
import collections
import geo_distance
import pprint

def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        coffee_reader = csv.reader(coffee_csv)
        pprint.pprint([row[0] for row in coffee_reader if row[0] == 'Espresso'])


def csv_airport(country):
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_row = next(airport_reader)
        print(airport_row)
        print([row[1] for row in airport_reader if row[3] == country])


def calc_airport_distances():
    airport_lats = {}
    airport_longs = {}
    stops = None
    
    with open("airports.csv") as airports_csv:
        airport_reader = csv.reader(airports_csv)
        airport_headers = next(airport_reader)
        for row in airport_reader:
            airport_lats[row[0]] = float(row[6])
            airport_longs[row[0]] = float(row[7])

    with open("routes.csv") as routes_csv:
        route_reader = csv.reader(routes_csv)
        route_headers = next(route_reader)
        
        for row in route_reader:
            source_id = row[3]
            dest_id = row[5]
            # print(row)
            if row[7] == 'Y':
                stops == True
            

            if source_id in airport_lats and dest_id in airport_lats:
                source_lat = airport_lats[source_id]
                source_long = airport_longs[source_id]
                dest_lat = airport_lats[dest_id]
                dest_long = airport_longs[dest_id]


                km_dist = geo_distance.distance(source_lat,
                                                source_long,
                                                dest_lat,
                                                dest_long)

                with open("dist_info.csv", "a") as dist_info:
                    dist_info_writer = csv.writer(dist_info)
                    dist_info_writer.writerow([source_id, dest_id, km_dist, stops])
                    
                





# csv_coffee()
# csv_airport('Japan')
calc_airport_distances()
