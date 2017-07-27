import csv
import geo_distance

def read_nohead(file):
    with open(file) as f:
        x = csv.reader(file)
        y = next(x)
        return x


def airports_info():
    '''
    :return: {airport ID: [(city, country), latitude, longitude, # of flights out of that airport]}
    '''
    d = {}
    with open('airports.csv') as f:
        airports = csv.reader(f)
        header = next(airports)

        for row in airports:
            if row[0] not in d:
                d[row[0]] = [(row[2], row[3]), float(row[6]), float(row[7]), 1]
            else:
                d[row[0]][3] += 1
        return d

def find_route_info():
    '''
    :return: [ [source airport ID, (its city, its country), # of flights out of that airport,
    distination ID, (its city, its country),
    flight distance, world rank of that flight distance] ]
    '''
    info = []
    d = airports_info()
    with open('routes.csv') as f:
        routes = csv.reader(f)
        header = next(routes)

        for row in routes:
            source, dest = row[3], row[5]
            if source in d and dest in d:
                source_list = d[source]
                dest_list = d[dest]
                source_lat, source_long = source_list[1], source_list[2]
                dest_lat, dest_long = dest_list[1], dest_list[2]
                info.append([source, source_list[0], source_list[3],
                         dest, dest_list[0],
                         geo_distance.distance(source_lat, source_long, dest_lat, dest_long), 0])
        add_distance_rank(info)
        return info

def add_distance_rank(l):
    i = 0
    distances = []
    while i < len(l):
        distances.append((l[i][5], i))
        i += 1
    distances.sort()
    i = 1
    j = 0
    old_value = 0
    for item in distances:
        k = item[1]
        if item[0] == old_value:
            l[k][6] += j
            i += 1
        else:
            j = i
            l[k][6] += j
            old_value = item[0]
            i += 1

route_info = find_route_info()

with open('more_route_info.csv', 'w') as f:
    info = csv.writer(f)
    info.writerow(('Source airport-ID', 'Source (City, Country)', 'Number of flights out of Source airport',
                   'Destination airport-ID', 'Destination (City, Country)',
                   'Flight distance', 'World distance rank'))
    for l in route_info:
        info.writerow((l[0], l[1], l[2], l[3], l[4], l[5], l[6]))


