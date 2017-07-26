import csv,geo_distance
def calc_airport_distances():
    # define two empty dicts that will hold our lat/long info
    airport_lats = {}
    airport_longs = {}

    with open("airports.csv") as f:
        # setup reader and remove header
        airport_reader = csv.reader(f)
        airport_headers = next(airport_reader)

        for row in airport_reader:
            try:
                airport_lats[row[0]] = float(row[6])
            except ValueError:
                print("Value not a float")
            else:
                airport_longs[row[0]] = float(row[7])

    # now that we have lookup dicts for lat/long loop through the routes
    with open("routes.csv") as f2:
        route_reader = csv.reader(f2)
        route_headers = next(route_reader)

        for row in route_reader:
            source_id = row[3]
            dest_id = row[5]


            # check to see if the ids for both airports are in the lookup dicts
            if source_id in airport_lats and dest_id in airport_lats:
                # use the lat/long dicts to get the coordinate info for each airport
                source_lat = airport_lats[source_id]
                source_long = airport_longs[source_id]
                dest_lat = airport_lats[dest_id]
                dest_long = airport_longs[dest_id]

                # make a variable that captures the output from the geo_distance function
                km_dist = geo_distance.distance(source_lat,
                                                source_long,
                                                dest_lat,
                                                dest_lat)

                # open a csv file that we want to append information to and write a row
                with open("air_dist.csv", "a") as f_3:
                    f_3_writer = csv.writer(f_3)
                    f_3_writer.writerow([source_id, dest_id, km_dist])


calc_airport_distances()