import requests
import json
from collections import defaultdict


def get_data():
    url_root = 'http://service.civicpdx.org/homeless/ethnicity/?'
    data = defaultdict(list)
    for year in range(1990, 2018):
        temp = []
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
            if temp == prev:
                print('no/dup data for year {} page {}'.format(year, page))
                break

            data[year].extend(temp)
    return data


def show_data_by(data, key):
    # data is: {year: [dictionaries of subcategory of homeless population]}
    # key is a datapoint in subcat: 'ethnicity', 'sheltertype'
    count_by_type = {}
    for year in data.keys():
        count_by_type[year] = defaultdict(int)
        people = 0
        for e in data[year]:
            # e is {subcategory of homeless pop}
            # e[key] is which subcategory
            count_by_type[year][e[key]] += e['count']
            people += e['count']

        print('year={}, #bins={}, people={}'.format(year,
                                                    len(data[year]),
                                                    people))
        print([item for item in count_by_type[year].items()])
        print()
    return count_by_type
