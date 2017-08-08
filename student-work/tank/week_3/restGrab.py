import requests
import json
import csv
total = 0

#all the people in all the shelters in range on page one extra credit
my_url = 'http://service.civicpdx.org/homeless/ethnicity/'
response = requests.get(my_url)
with open('homeless.csv', 'w') as fout:
    writer = csv.writer(fout)
    for i in range(2000,2017):
        r = requests.get(my_url+f'?format=json&page=1&year={i}')
        print( r.content.decode())
        for x in r.json():
            total += x.get('count')
        kount += total
    print(total, kount, i)
    
    counts = sum([d.get('count') for d in ans])
    print (i, total)
    writer.writerow(i,total)
