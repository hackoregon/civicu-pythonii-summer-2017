# 1) load the json from a civicpdx.org response into a list or dictionary, 2)
# extract an integer from it for the "count" of homeless people in a shelter for each year in your loop, 3) sum up all those counts
# for all the years in civicpdx
# this will require you to iterate through the list of dictionaries (one dictionary for each shelter type) that is
## returned with each request and use the `{}.get('count', 0)` method on each dictionary. This will make
## `get()`return a 0 if the "count" key doesn't exist in the' \     ' dictionary. You can then do a `sum()` on all those integers to sum up the count of all the homeless people surveyed for that year in Portland.


import json
import requests
import csv
'''
for i in range(2000, 2016):
    url = 'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={}'.format(i)
    r = requests.get(url)
    print(r.status_code)
    print(json.loads(r.content.decode()))
'''

with open("pdx_homeless_count.csv", "w") as f:
    writer = csv.writer(f)
    total = 0 #placement of total is important. will only yield last value if out of the loop :*(
    for i in range(2000, 2016):
        url = f'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={i}' #f-strings are v3.6 only
        r = requests.get(url)
        response_dict = r.json()
        #print(json.dumps(response_dict, indent=2)) #beautify your Json with .dumps()

        if response_dict:
            #print(response_dict[0]['count']) #index and k: will spit out v
            each_year = sum([x.get('count', 0) for x in response_dict])
            total += each_year
            #print(i, each_year)
            writer.writerow([i, each_year])
            print(total)
        else:
            print(f"No data was available for year {i}")


print(f"There are {total} homeless people in PDX")



