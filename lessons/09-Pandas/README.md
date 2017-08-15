# Data Wrangling (Pandas)

- Review DB and SQL skills
- Review building DRF APIs
- Enhance our DRF API with a POST (upload)
- Explore Pandas

We're going to spend some more time today talking about data, retrieving it and inserting it into a DB, and changing/cleaning it. This is called "Data Wrangling" within the Data Science and DB Engineering world.

## Survey Review

The results are in... with a lot of good ideas for improving the course.

- More homework
- More challenging classwork
- More structure


## Database Review

So let's go back over what you learned last week to make sure we're maintaining structure, consitency.

- What is `csvkit`?
- What is `agate`?
- What do you like about them?
- What do you not like or wish they could do?


### Django `filter`

Let's continue Mark's Django ORM `filter` discussion.


## DRF Review

In the interest of closure and better structure, consistency, let's review our labeler API code to get the *R* in C*R*UD working.
Then we can add a new features to enable programatic upload of images through the API make sure we can use it to upload data for the *CR* part of CRUD in our API.


### DRF `settings.py`

We need to install `rest_framework` in our `settings.INSTALLED_APPS` before Django can find the templates folder it needs to render our views, like our list view.

```python
INSTALLED_APPS = [
    'labeler.apps.LabelerAppConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
]
```

### Serializer uses `fields = '__all__'`

Zak's approach greatly simplifies the `Serializer` by taking advantage of some of the DRF ModelSerializer meta features.

```python
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
```

### Enable the *C* in *C*RUD by changing our base generic type for the view so it responds to a POST

In `views.py` notice that `ListAPIView` has been changed to `ListCreateAPIView`.

```python
class ListImages(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
```

### Using POST to upload pictures

[This StackOverflow question](https://stackoverflow.com/questions/20217348/requests-post-files-upload-large-file-more-than-1-5-mb-python) can help you compose a POST request that interacts with a "FileField" to upload an image.

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

### Exercise

Incorporate this into your bot's skills by adding an argument to the argparser to upload an image file from your computer to your API.

You can see how I started to implement mine [here](https://github.com/totalgood/civicu_app/blob/e343a7380754fa563f43f85957473ea32ecab318/labeler_site/bot.py)

And atttempt two more exercism exercises.



## Pandas

Pandas is a data table wrangling and visualization library. It's a lot like `csvkit` and `agate`, only more powerful. It has a lot of import export features for formats like CSV, JSON, XML, HTML, and even SQL so it's useful as a translator between data formats. And it can produce beautiful plots.
