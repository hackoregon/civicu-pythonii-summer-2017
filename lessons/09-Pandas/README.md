# Pandas

## DRF Review

### Need to install `rest_framework` in our `settings.INSTALLED_APPS`

```python

```

### Zak's example uses the `fields = '__all__'` which simplifies the `Serializer`


```python

```

### Enable the *C* in *C*RUD by changing our base generic type for the view so it responds to a POST


```python

```

### Using POST to upload pictures

```python
>>> POST_data = {'caption': 'posted bear', 'uploaded_by': 1}
>>> files = {'file': ('barlow-rd-2014-a-095_30343888245_o.jpg', open('/home/hobs/Pictures/bear/barlow-rd-2014-a-095_30343888245_o.jpg', 'rb')), 'file_name': 'barlow-rd-2014-a-095_30343888245_o.jpg'}
>>> resp = requests.post('http://localhost:8000/api/', data=POST_data, files=f)
>>> resp
```

Isn't that cool!

Now you can cycle through an entire directory of Pictures and upload them to your labeler app.

Let's get some paths and URLs for your system:

```python
>>> import requests

>>> url = 'http://localhost:8000/api/'  # 'http://3c27c00c.ngrok.io/api/'
>>> base_dir = os.path.join(os.getenv('HOME'), 'Pictures')
```

Now let's walk the entire tree of files and push them up to our server.


```python
>>> for dirname, dirnames, filenames in os.walk(base_dir):
...     # print path to all subdirectories first.
...     for subdirname in dirnames:
...         print(os.path.join(dirname, subdirname))
... 
...     # print path to all filenames.
...     for filename in filenames:
...         if not filename[-4:].lower() in ['jpeg', '.jpg', '.png', '.bmp']:
...             continue 
...         filepath = os.path.join(dirname, filename)
...         print(filepath)
...         with open(filepath, 'rb') as fin:
...             POST_data = {'caption': 'automatic upload of local path {}'.format(filepath)}
...             files_data = {'file': (filename, fin), 'file_name': filename}
...             resp = requests.post(url, data=POST_data, files=files_data)
...             print(resp)
...         break  # don't do this for *ALL* your files

```

## Database Review

- What is `csvkit`?
- What is `agate`?
- What do you like about them?
- What do you not like or wish they could do?

## Survey Review

- More homework
- More challenging classwork
- More structure

## Pandas

Pandas is a data table wrangling and visualization library. It's a lot like `csvkit` and `agate`, only more powerful. It has a lot of import export features for formats like CSV, JSON, XML, HTML, and even SQL so it's useful as a translator between data formats. And it can produce beautiful plots.
