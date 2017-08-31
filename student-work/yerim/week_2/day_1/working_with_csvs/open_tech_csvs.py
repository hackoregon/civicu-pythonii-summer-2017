# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work.

import csv
import glob
import geo_distance

csv_files = glob.glob('*.csv')

def coffee_reader():
    with open('coffee.csv', 'r') as f:
        f_reader = csv.reader(f)
        [print(row) for row in f_reader if row[0] == 'Long Black']


def make_airport_dict():
    with open('airports.csv', 'r') as f:
        f_reader = csv.reader(f)
        headers = next(f_reader)

        # key airport ID 1st column
        loc_dict = {int(line[0]):line[6:8] for line in f_reader}

        return loc_dict


def route_reader(loc_dict):
    distances = []
    with open('routes.csv', 'r') as routes:
        route_reader = csv.reader(routes)
        routes_header = next(route_reader)

        no_id = 0

        for line in route_reader:
            try:
                origin_loc = int(line[3])
                dest_loc = int(line[5])

                # find locations in the dictionary
                lat1 = float(loc_dict[origin_loc][0])
                long1 = float(loc_dict[origin_loc][1])
                lat2 = float(loc_dict[dest_loc][0])
                long2 = float(loc_dict[dest_loc][1])

                # find the distance and put it in a list
                dist = geo_distance.distance(lat1, long1, lat2, long2)

                distances.append([origin_loc, dest_loc, dist])

            except:
                no_id +=1

    return(distances)


def write_dist(dist_csv, dist_data):
    with open(dist_csv, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in dist_data:
            writer.writerow([s for s in line])




# for csv_file in csv_files:
#     if 'coffee' in csv_file:
#         coffee_reader()
#
#     elif 'airport' in csv_file:
#         airport_reader()

airport_dict = make_airport_dict()

distances = route_reader(airport_dict)

write_dist('distances_only.csv', distances)