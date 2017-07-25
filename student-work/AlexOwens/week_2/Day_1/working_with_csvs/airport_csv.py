# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:54:50 2017

@author: Alex
"""

import csv
import collections
import geo_distance


 
   
def calc_airport_distances():
    
    with open("airports.csv") as airport: 
        airport_reader = csv.reader(airport)
        airport_headers = next(airport_reader)
    
        
        lat_dict = {}
        long_dict = {}

    
        for row in airport_reader:
            lat_dict[int(row[0])] = float(row[6])
    
            long_dict[int(row[0])] = float(row[7])
            
 
        
        with open("routes.csv") as routes:
            routes_reader = csv.reader(routes)
            routes_header = next(routes_reader)
            
            dest_id = []
            source_id = []
            no_dest_id = 0

            i=0
            for row in routes_reader:
               
               if row[3] and row[5] != '\N':
                try:
                    dest_id.append(int(row[3]))
                    source_id.append(int(row[5]))
                    i += 1
                except ValueError:
                    no_dest_id += 1
            
            
            i = 0
           
            for key in dest_id:
              
              if key in lat_dict and source_id[i] in lat_dict: 
                  try: 
                      airport_dist= (geo_distance.distance(lat_dict[key], long_dict[key], lat_dict[source_id[i]], long_dict[source_id[i]]))
                      i += 1
                      print airport_dist
                  except KeyError:
                      pass
              else:
                  i += 1
calc_airport_distances()   
