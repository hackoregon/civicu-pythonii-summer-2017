import csv
import geo_distance

def find_airports(city):
    with open("airports.csv") as file:
        reader = csv.reader(file)

        header = next(reader)
        print(header)

        for row in reader:
            if row[2] == city:
                print(row)

find_airports('New York')

def distance(city1, city2):
    with open("airports.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[2] == city1:
                city1_lat = row[6]
                city1_long = row[7]
            elif row[2] == city2:
                city2_lat = row[6]
                city2_long = row[7]

        try:
            city1_lat
        except NameError:
            print("Oops, couldn't find that city.")
            return

        try:
            city2_lat
        except NameError:
            print("Oops, couldn't find that city.")
            return

        city1_lat = float(city1_lat)
        city1_long = float(city1_long)
        city2_lat = float(city2_lat)
        city2_long = float(city2_long)

        result = geo_distance.distance(city1_lat, city1_long, city2_lat, city2_long)
        row = [city1, city2, result]

    with open('result.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)

distance('Boston', 'Paris')
