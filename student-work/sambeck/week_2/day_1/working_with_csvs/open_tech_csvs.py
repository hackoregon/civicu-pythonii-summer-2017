# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory

# just please try to remember not to commit the csv files when you're saving 
# your work. 


import csv
import geo_distance


# print all airports in a country
def print_airports(country):
    with open('airports.csv') as air:
        airports = csv.reader(air)
        next(airports)  # delete header
        # print(header)
        count = 0
        for row in airports:
            if row[3] == country:
                print(row)
                count += 1
        print('There are {} airports in {}!'.format(count, country))


# save from csv to dictionary, key = airport id, value = (lat, long)
def get_airport_coords():
    with open('airports.csv') as air:
        airports = csv.reader(air)
        next(airports)
        coords = {}
        names = {}
        for row in airports:
            try:
                coords[row[0]] = (float(row[6]), float(row[7]))
                names[row[0]] = row[1]
            except:
                print('cannot convert to float')
        print('Loaded coordinates/names of {} airports.'.format(len(coords)))
        print('')
        return coords, names


# save routes from .csv to list
def get_routes():
    simple_routes = []
    with open('routes.csv') as r:
        routes = csv.reader(r)
        next(routes)
        for route in routes:
            simple_routes.append([route[3], route[5]])
    print('Loaded {} routes'.format(len(simple_routes)))
    print('')
    return simple_routes


# save distances from routes to a new list of distances, indexed
def get_distances(routes, names, coords):
    distances = []
    errors = 0
    for row in routes:
        a1, a2 = row[0], row[1]
        # print(a1, a2)
        try:
            (lat1, long1) = coords[a1]
            (lat2, long2) = coords[a2]
        except KeyError:
            # print('fail on key 1: {}'.format(a1))
            distances.append('airport not found: {}'.format(a1))
            errors += 1
            continue
        distances.append(geo_distance.distance(lat1, long1, lat2, long2))
    print('Found distances of {} routes with {} errors.'.format(len(distances),
                                                                errors))
    print('EX:')
    print('First route: {}'.format(routes[0]))
    print_distance(routes[0], distances[0], names)
    return distances


# function prints out a route for human reading
def print_distance(route, distance, names):
    # {:.7f} is 7 decimal digits
    print('From {} to {}, distance is {:.2f} km'.format(names[route[0]],
                                                        names[route[1]],
                                                        distance))
    print('')


# write routes with distances to .csv
def write_distances(distances, routes, filename='route_distances.csv'):
    row_format = ['airport ID #1', 'airport ID #2', 'distance (km)']
    if len(distances) != len(routes):
        raise ValueError('length mismatch!')
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(row_format)
        for i in range(len(routes)):
            writer.writerow(routes[i] + [distances[i]])
    print('Done writing {} values to {}'.format(len(routes), filename))
    print(row_format)
    print('')


def check_csv(names, filename='route_distances.csv'):
    with open(filename) as f:
        csvreader = csv.reader(f)
        print('opening: ' + filename + ', first two rows:')
        print(next(csvreader))
        row1 = next(csvreader)
        print_distance(row1[:2], float(row1[2]), names)
        i = 0
        for row in csvreader:
            i += 1
        print('plus there are {} additional rows.'.format(i))
        print()


# execute whole program
def do_program():
    coords, names = get_airport_coords()
    routes = get_routes()
    distances = get_distances(routes, names, coords)
    write_distances(distances, routes)
    check_csv(names)


if __name__ == '__main__':
    do_program()

