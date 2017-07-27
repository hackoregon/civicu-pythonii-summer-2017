import requests
import json
#all the people in all the shelters in range on page one extra credit
my_url = 'http://service.civicpdx.org/homeless/ethnicity/'
response = requests.get(my_url)
#for i in range(2000,2015):
r = requests.get(my_url+'?format=json&page=1&year=2015')
print( r.content.decode())
#print(json.JSONEncoder(r.raw))
