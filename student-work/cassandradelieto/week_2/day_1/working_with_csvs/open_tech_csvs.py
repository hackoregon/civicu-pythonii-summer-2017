
# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 

import csv
import geo_distance


def csv_airport(city):
    with open("airports.csv", encoding="utf8") as f:  # STACKOVERFLOW: file in question is not using the CP1252 encoding. Try Latin-1 OR UTF-8
        airport_list = []
        airport_reader = csv.reader(f)
        for row in airport_reader:
            if row[2] == city:
                airport_list.append(row)
            #else:
                #print("Please pick a valid city name. Did you spell it correctly?") THIS DOESN'T WORK. PRINTS REGARDLESS SINCE IT CYCLES THROUGH EVERY CITY.
        return airport_list


def calc_airport_distances(origin, destination):
    origin_city = csv_airport(origin)
    destination_city = csv_airport(destination)
    rows = []
    for airport1 in origin_city:
        for airport2 in destination_city:
            lat_origin = float(airport1[6])
            long_origin = float(airport2[7])
            lat_destination = float(airport2[6])
            long_destination = float(airport2[7])

        km_dist = geo_distance.distance(lat_origin, long_origin, lat_destination, long_destination)
        rows.append([origin, airport1[1], destination, airport2[1], km_dist])  # for the csv

        print("The distance from {}'s {} to {}'s {} in kilometers is {}".format(origin, airport1[1], destination, airport2[1], km_dist))

    with open('distances.csv', 'w') as file:
        write = csv.writer(file)
        header = ['Departing', 'Departing Airport', 'Arriving', 'Arriving Airport', 'Difference in KM']
        write.writerow(header)
        for row in rows:
            write.writerow(row)


# airport_dict = collections.defaultdict(int)
#       try:  # how many are bad keys?
#          print(lat_dict[dest_id])
#      except KeyError:
#          no_id += 1
# print(no_id)


calc_airport_distances("Miami", "Chicago")

