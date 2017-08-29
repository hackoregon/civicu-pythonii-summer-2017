

```python
import requests
import json
import csv

with open('homeless.csv', 'w') as fout:
    writer = csv.writer(fout)
    total = 0
    for i in range(2000, 2016):
        resp = requests.get('http://service.civicpdx.org/homeless/ethnicity/?page=1&year={i}'.format(i=i))
        ans = resp.json()
        # print(json.dumps(ans, indent=2))
        if ans:
            # BONUS: FIXME: look closely at the dictionaries to make sure we aren't double-counting!
            year_total = sum([d.get('count', 0) for d in ans])
            total += year_total
            print(i, year_total)
            writer.writerow([i, year_total])
    print(total)
```


```python
import json
import requests

for i in range(2000, 2015):
    url = 'http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year={}'.format(i)
    print(url)
    r = requests.get(url)
    print(r.status_code)
    print(json.dump(json.loads(r.content.decode()), indent=2))
```

    http://service.civicpdx.org/homeless/ethnicity/?format=json&page=1&year=2000
    200



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-b6a60a5cbb89> in <module>()
          7     r = requests.get(url)
          8     print(r.status_code)
    ----> 9     print(json.dump(json.loads(r.content.decode()), indent=2))
    

    TypeError: dump() missing 1 required positional argument: 'fp'



```python

```
