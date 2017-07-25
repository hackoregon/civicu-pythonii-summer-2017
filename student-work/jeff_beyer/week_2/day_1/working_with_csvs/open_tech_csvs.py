# to use the csvs in the class's shared-resoruces directory you'll need to
# either reference them by uning a relative path
# Ex. "../../../../../shared-resources/<csv_file_name>.csv"
# or if you prefer you can make a copy and move the files into this directory
# just please try to remember not to commit the csv files when you're saving 
# your work. 

import csv
from geo_distance import distance

#def csv_coffee():
#    with open('coffee.csv', 'r') as f:
#        reader = csv.reader(f)
#
#        #for row in reader:
#        #    print(row)
#
#        [print(row) for row in reader if row[0] == 'Espresso']

# Airport.csv Headers: 
# ['ID', ' Airport-Name', ' City', ' Country', ' IATA', ' ICAO', ' Latitude', ' Longitude', ' Altitude', ' Timezone', ' DST', ' Tz-Type', ' Source']

# routes.csv Headers:
# Airline, Airline-ID, Source-airport, Source-airport-ID, Destination-airport, Destination-airport-ID, Codeshare, Stops, Equipment
# def csv_airport():
#     with open('airports.csv') as f:
#         reader = csv.reader(f)

#         header = next(reader)
#         print(header)

def print_airport():
    # initialize lat and lon dictionaries
    lat = dict()
    lon = dict()
    # Open the airports.csv file to read lat and lon for each aiport (store 
    # airport ID as int as dict key
    with open('airports.csv') as fin:
        reader = csv.reader(fin)
        header = next(reader)

        # Latitude is index 6, longitude is index 7
        for row in reader:
            lat[int(row[0])] = float(row[6])
            lon[int(row[0])] = float(row[7])

    # Now open the dists.txt file for writing out the distance calculations
    with open('dists.txt', 'w', newline='') as fout:
        writer = csv.writer(fout)
        # Write a header line
        writer.writerow(('Start-Airport-ID','End-Airport-ID','Distance'))
        # Open the routes.csv to see what distances to calculate
        with open('routes.csv') as f:
            reader = csv.reader(f)
            header = next(reader)
            # Read the file
            for row in reader:
                # Start ID is index 3, dest ID is index 5
                try:
                    # Attempt to pull the start_id and end_id
                    start_id = int(row[3])
                    end_id = int(row[5])
                except ValueError:
                    # Skip it if there's an issue with the value
                    continue
                
                try:
                    # Attempt to calculate the distance 
                    dist = distance(lat[start_id], lon[start_id], lat[end_id], 
                        lon[end_id])
                except KeyError:
                    # But if that fails skip it
                    continue
                # write out the start_id, end_id and distance
                writer.writerow((f'{start_id}', f'{end_id}',f'{dist}'))
                

                
print_airport()