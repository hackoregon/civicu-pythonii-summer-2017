import json
import requests


def how_many_homeless():
    count = 0
    for year in range(2007, 2017, 2): # increment by 2 since there's only odd years
        url = f'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={year}'
        r = requests.get(url)
        if r.status_code == 200: # make sure your internet is working and url's haven't changed
            data = json.loads(r.content.decode())
            if data:
                count += sum([entry['count'] for entry in data])

    return count

homeless_count = how_many_homeless()
print(f'{homeless_count} total homeless people in Portland over the years')

# 18,210 is the answer

