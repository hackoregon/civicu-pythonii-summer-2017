# Django ORM

## Querying with Django ORM

### `QuerySet` (`django.db.models.query.QuerySet`)

This is how you can retrieve an iterable that points back to a table in Django:

```python
>>> from freegeek.models import Sale
>>> qs = Sale.objects.all()
```

`.objects` is that QuerySet manager for the DB table and Django model called `Sale`.
The manager is responsible for being efficient about writing and running SQL queries to retrieve records from the database tables when you ask for them.
Actually it does nothing when you first ask for them, it waits until the last possible moment when you try to access a particular record.
This is called "lazy evaluation."
In manufacturing it's called "JIT manufacturing" because the production line is tied directly to the sales channel and is optimized to make sure the backlog of unsold stock is always zero.
They can slow or speed up the production line for individual products to match demand and only build something right before they ship it.

Likewise in complied programming languages it's called "JIT compiling."
Your code isn't compiled until you run it.

Django does this with the SQL code it generates from your queries.
It'll generate multiple SQL commands for each Django ORM query you write, and it'll run the fastest one that gets you whatever records you asked for.
A queryset works like a generator, grabbing a few items at a time from the database when you need them.

### `count()` vs `len()`

Probably the simplest query is to count up the records in a table, like using `len()` on a `pd.DataFrame` or a `list`.
But you don't ever ask for the `len(qs)`, because Django doesn't know yet and would have to iterate through them all.
For the half million records in the FreeGeek Sale table this takes several seconds:

[TIP]: Don't do this!

```python
>>> len(qs)
548842
```

[TIP]: Do this!

```python
>>> qs.count()
548842
```

The `count()` method takes milliseconds on the largest databases because it runs the query in SQL instead of python, using the database index which usually has a count of the records precomputed and stored somewhere.

### `filter`

The `.filter()` method of a `QuerySet` is the equivalent of SQL's `WHERE` keyword.
So let's us it to count up something more interesting, a filtered list of those Sales at Free Geek.
The filter syntax will feel weird at first, because Django reads your kwargs dynamically and creates logic based on what their names are in the `**kwargs`. It looks for suffixes like these to do inequality filters:

- `__gt`, `__lt`, `__gte`, `__lte`
- `__isnull`, `__notnull`
- `__icontains`, `__contains`

If you don't proved a suffix, then the query is assumed to be an "equals" query. 

Django looks for field names of foreign key records after the dunder (`__`) symbol also.
So 'Image.filter(user__id=2)' will return all the Image records that are associated with the `User` record that has an `id` field with a value of 2.


```python
>>> from freegeek import Sale
>>> import datetime
>>> Sale.objects.filter(created_at__gt=datetime.datetime(2017,1,1)).count()
/home/hobs/.virtualenvs/freegeek/local/lib/python2.7/site-packages/django/db/models/fields/__init__.py:1474: RuntimeWarning: DateTimeField Sale.created_at received a naive datetime (2017-01-01 00:00:00) while time zone support is active.
  RuntimeWarning)
```

To fix this warning, we need to always use dates with a timezone when working with a Django project where the TIMEZONE setting has been set.


```python
>>> import pytz
>>> tzinfo = pytz.timezone('US/Pacific')
>>> Sale.objects.filter(created_at__gt=datetime.datetime(2017, 1, 1, tzinfo=tzinfo).count()

```

### `annotate` and `Count`

```python
>>> from pprint import pprint
>>> counts = qs.filter(created_at__gt=jan1).values('cashier_created_by_id').annotate(count=Count('cashier_created_by_id'))
>>> pprint(list(counts))
```

## Schemaless Django

Our images are going to have a lot of metadata associated them.
We probably want things like the camera type, focal length, and GPS coordinates for any images that have them.
This is available in the EXIF headers of most images.
But we don't know the "schema" of this data ahead of time.
Each camera manufacturer can do things differently.
So we can create "schemaless" records in our DB for just this purpose.

### JSONField

Django has a JSONField that is kind-of like an image blob, where django just maintains a pointer to our json file.
But this time, unlike a `FileField` Django will actually index it (look inside the file) to allow us to query based on the fields inside the JSON.

Let's create a JsonField on our Image table to store all this data.
This will be useful for your application even if you aren't working with images.
Your Poll questions or labeled objects almost certainly have a lot of metadata that you aren't sure about its schema right now, but you want to be able to display it with your object in your app.

Unfortunately JSONField is new to Django 1.11 and is only available if you are using the `psycopg2` backend for PostGRESQL.
Since we're using SQLite we need to install a django package that has a JSONField with similar functionality.

```bash
pip install jsonfield
```

Whenever you do a pip install, what else should you do immediately after it?

```bash
pip freeze | grep jsonfield >> 'requirements.txt'
```

Let's add a `JSONField`:

```python
import jsonfield

class Image(models.Model):
    """ A database record for images to be labeled """
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512, default=None, null=True)  # , required=False)
    taken_date = models.DateTimeField('Date photo was taken.', null=True, default=None)
    updated_date = models.DateTimeField('Date photo was changed.', auto_now=True)
    created_date = models.DateTimeField('Date photo was created.', auto_now_add=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)  # , required=False)
    file = models.FileField("Image to be labeled", upload_to='images')
    info = jsonfield.JSONField("Metadata about the image (usually from the EXIF header)", null=True)
```

And then let's give it some data:

```python
>>> import random
... for image in Image.objects.all():
...     image.info = {'alt': random.randint(500, 5000)}
...     image.save()
```

This means we could look for all the pictures taken above 4000 ft on Mt Hood (if the EXIF data contained it) with a query like this:

```python
>>> images = Image.objects.filter(info__contains='"alt":')
>>> images.count()
16
>>> high_images = Image.objects.filter(info__contains='"alt": 4')
>>> high_images.count()
4
```

So this points out the disadvantage of schemaless jsonfields for non-postgresql databases.
You have to use inefficient queries on the strings rather than indexed queries on the values directly.

Here's some code to create more complex conditions for json fields:

```python
def make_cond(name, value):
    from django.utils import simplejson 
    cond = simplejson.dumps({name:value})[1:-1] # remove '{' and '}'
    return ' ' + cond # avoid '\"'
```

[TODO]: test this

