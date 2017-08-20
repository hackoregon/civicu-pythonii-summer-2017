

```python
import requests
import os

base_dir = os.path.join(os.getenv('HOME'), 'Pictures')
url = 'http://localhost:8000/api/'
filename = 'barlow-rd-2014-a-095_30343888245_o.jpg'
with open(os.path.join(base_dir, 'bear', filename), 'rb') as fin:
    print(fin.name)
    POST_data = {'caption': 'posted bear'}
    files = {'file': (filename, fin),
             'file_name': filename}
    resp = requests.post(url, data=POST_data, files=files)
    print(resp)
```

    /home/hobs/Pictures/bear/barlow-rd-2014-a-095_30343888245_o.jpg
    <Response [201]>

