# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 

import csv
import geo_distance


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
        print('There are {} airports in {}!'.format(count, country))


def get_airport_coords():
    with open('airports.csv') as air:
        airports = csv.reader(air)
        header = next(airports)
        print(header)
        coords = {}
        # print(header)
        for row in airports:
            coords[row[0]] = (float(row[6]), float(row[7]))
    return coords


def get_routes():
    simple_routes = []
    with open('routes.csv') as r:
        routes = csv.reader(r)
        x = next(routes)
        print(x)
        for route in routes:
            simple_routes.append((route[3], route[5]))
    return simple_routes


def get_distances(routes, coords):
    distances = []
    for row in routes:
        a1, a2 = row[0], row[1]
        # print(a1, a2)
        try:
            (lat1, long1) = coords[a1]
        except KeyError:
            print('fail on key')
            continue
        try:
            (lat2, long2) = coords[a2]
        except KeyError:
            print('fail on key')
            continue
        distances.append(geo_distance.distance(lat1, long1, lat2, long2))
    print(distances)


def write_distances(distances, routes):
    c = csv.writer('route_distances.csv', 'w')
    num = 0
    with open(c) as w:
        for i in range(len(routes)):
            w.write(routes[i], distances[i])
            num = i
    print('Done writing {} values to {}'.format(num, c))


if __name__ == '__main__':
    coords = get_airport_coords()
    routes = get_routes()
    distances = get_distances(routes, coords)
    
