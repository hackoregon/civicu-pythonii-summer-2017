# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 


import csv
import geo_distance
import collections




# add a link or pic to the readme with the flags you can pass in to the open() func
def csv_coffee():
    with open("coffee.csv") as coffee_csv:
        my_reader = csv.reader(coffee_csv)
        for row in my_reader:
            print(row)

#csv_coffee()

def print_rows(country):
    with open("airports.csv") as f:
        airports = csv.reader(f)
        header = next(airports)
        for row in airports:
            if row[3] == country:
                print(row)

#print_rows('United States')

def count_airports_in_country(country):
    with open("airports.csv") as f:
        airports = csv.reader(f)
        header = next(airports)
        n = 0
        for row in airports:
            if row[3] == country:
                n += 1
    return n

#print(count_airports_in_country('Canada'))


def flight_distances():
    latitudes = {}
    longitudes = {}
    with open("airports.csv") as file:
        airports = csv.reader(file)
        airport_headers = next(file)
        for row in airports:
            latitudes[row[0]] = float(row[6])
            longitudes[row[0]] = float(row[7])

    flights = []
    with open("routes.csv") as file:
        routes = csv.reader(file)
        route_headers = next(file)
        for row in routes:
            flights.append((row[3], row[5]))
    flight_distances = []
    bad_rows = []
    #values = []
    for (origin, destination) in flights:
        try:
            lat1, long1, lat2, long2 = latitudes[origin], longitudes[origin], latitudes[destination], longitudes[destination]
            flight_distance = geo_distance.distance(latitudes[origin], longitudes[origin], latitudes[destination], longitudes[destination])
            flight_distances.append((origin, destination, flight_distance))
        except KeyError:
            bad_rows.append((origin, destination))
            '''
            The code below enables us to see why the distances for some rows can't be calculated: they involve airports that aren't listed in airports.csv
            a, b, c, d = origin in latitudes.keys(), origin in longitudes.keys(), destination in latitudes.values(), destination in longitudes.values()
            values.append((a, b, c, d))
            COULD'VE JUST DONE "pass"
            '''

    return flight_distances


distances = flight_distances()

#    WRITES DISTANCES TO A CSV FILE
with open('flight_distances.csv', 'w') as csvfile:
    the_writer = csv.writer(csvfile)
    the_writer.writerow(['Source-airport-ID', 'Destination-airport-ID', 'Distance'])
    for item in distances:
        the_writer.writerow([item[0], item[1], item[2]])
