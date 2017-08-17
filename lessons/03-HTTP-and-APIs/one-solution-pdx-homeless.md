

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

    2009 2265
    2011 7273
    2013 7107
    2015 1565
    18210



```python

```
