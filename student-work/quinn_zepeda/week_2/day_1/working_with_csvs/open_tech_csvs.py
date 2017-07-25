import csv
import collections
import geo_distance

##with open('coffee.csv') as foo:
##    foo = csv.reader(foo)
##    for row in foo:
##        print(row)

def csv_airport():
    with open('airports.csv') as airport_csv:
        airport_reader = csv.reader(airport_csv)
        airport_header = next(airport_reader)
        print(airport_header)

 
        for row in airport_reader:
            if row[3] == "Albania":
                print(row)
            


def calc_airport_distances():
    airport_lats = {}
    airport_longs = {}
    
   with open('airports.csv') as airports_csv:
        airport_reader = csv.reader(airports_csv)
        route_header = next(airport_reader)
        

       for row in airport_reader:
            airport_lats[row[0]] = float(row[6])
            airport_longs[row[0]] = float(row[7])
            

   with open('routes.csv') as route_csv:
        route_reader = csv.reader(route_csv)
        route_header = next(route_reader)

       for row in route_reader:
            source_airport = row[2]
            source_id = row[3]
            dest_airport = row[4]
            dest_id = row[5]

           if source_id in airport_lats and dest_id in airport_longs:
                # use the lat/long dicts to get the coordinate info for each airport
                source_lat = airport_lats[source_id]
                source_long = airport_longs[source_id]
                dest_lat = airport_lats[dest_id]
                dest_long = airport_longs[dest_id]

               km_dist = geo_distance.distance(source_lat, source_long, dest_lat, dest_long)

               with open("dist_info.csv", "a") as dist_info:
                    dist_info_writer = csv.writer(dist_info)
                    dist_info_writer.writerow([source_airport, dest_airport, km_dist])



calc_airport_distances()
