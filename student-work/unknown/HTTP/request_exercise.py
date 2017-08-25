import requests
import json
import csv

# y = 'year'
# s = '='

# for i in range(start, end):
#     '{}{}{}'.format(y, s, i)

start = 2005
end = 2017
counts_per_year = []
# for page 1, count all of the homeless people in all the shelters, for a range of years
for i in range(start, end):
    url = 'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={}'.format(i)
    r = requests.get(url)

    # this is a list of dictionaries
    homeless = r.json()

    if homeless:
        count = sum([d.get('count', 0) for d in homeless])

        # save to a list (will write to a csv later)
        line = ['{} {}'.format(i, count)]
        counts_per_year.append(line)


with open('homeless_count_per_year.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['year', 'number of homeless for the year'])
    for line in counts_per_year:
        writer.writerow([s for s1 in line for s in s1.split()])