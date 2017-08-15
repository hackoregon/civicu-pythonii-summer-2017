# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving
# your work.


import csv
import geo_distance


def find_airports(city):
    with open("airports.csv") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            if row[2] == city:
                list.append(row)
        return list

def distance(city1, city2):
    # Get lists of possible airports
    city1airports = find_airports(city1)
    city2airports = find_airports(city2)

    # Make sure we actually got airports
    if len(city1airports) == 0 or len(city2airports) == 0:
        print("Couldn't find an airport for ya, bud.")
        return

    # Create rows to write later
    new_rows = []
    for airport1 in city1airports:
        for airport2 in city2airports:
            city1_lat = float(airport1[6])
            city1_long = float(airport1[7])
            city2_lat = float(airport2[6])
            city2_long = float(airport2[7])

            result = geo_distance.distance(city1_lat, city1_long, city2_lat, city2_long)
            new_rows.append([city1, airport1[1], city2, airport2[1], result])

    with open('result.csv', 'w') as file:
        writer = csv.writer(file)

        header = ['Departing City', 'Departing Airport', 'Arriving City', 'Arriving Airport', 'Distance (km)']
        writer.writerow(header)

        for row in new_rows:
            writer.writerow(row)

distance('New York', 'Paris')
