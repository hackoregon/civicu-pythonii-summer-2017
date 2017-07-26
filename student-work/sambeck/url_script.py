import requests
import json

url_root = 'http://service.civicpdx.org/homeless/ethnicity/?'

data = {}
temp = []
for year in range(1990, 2018):
    for page in range(1, 11):
        query = url_root + 'year={}&page={}&format=json'.format(year, page)
        response = requests.get(query)
        print('\n year={} page={}'.format(year, page))
        print(response.status_code)
        # print(response.headers)
        # print(response.content)

        prev = temp
        temp = json.loads(response.content.decode())
        # print(temp)
        if temp == []:
            print('no data for year {} page {}'.format(year, page))
            break
        if temp == prev:
            print('page {} is duplicate for year {}'.format(page, year))
            break

        if year not in data:
            data[year] = temp
        else:
            data[year].append(temp)


people_in_year = {}
for year in data.keys():
    people = 0
    for shelter in data[year]:
        people += shelter['count']

    people_in_year[year] = people
    print('year={}, # shelters={}, people={}'.format(year,
                                                     len(data[year]),
                                                     people))

