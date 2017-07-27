import json
import requests

def how_many_homeless():
    total_count = 0
    for i in range(2001, 2015, 2):
        url = 'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={}'.format(i)
        r = requests.get(url)
        data = json.loads(r.content.decode())
        if data:
            total_count += data[0]['count']
    return total_count

print('{} total homeless people in Portland.'.format(how_many_homeless()))

