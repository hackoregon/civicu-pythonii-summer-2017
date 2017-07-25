import requests
import json

url_root = 'http://service.civicpdx.org/homeless/ethnicity/?'

data = {}
for year in [2009, 2011, 2013, 2015]:
    for page in range(1, 2):
        query = url_root + 'year={}&page={}&format=json'.format(year, page)
        response = requests.get(query)
        print('\n' + str(year))
        print(response.status_code)
        print(response.headers)
        print(response.content)
        data[year] = json.loads(response.content.decode())

people_in_year = {}
for year in data.keys():
    people = 0
    print(year)
    for shelter in data[year]:
        people += shelter['count']
    people_in_year[year] = people

print(people_in_year)
