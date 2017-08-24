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
So you don't ever ask for the `len(qs)` , because Django doesn't know yet and would have to iterate through them all.
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

But


### `count`

First let's just count up the records in a table.

```python
>>> from freegeek.models import Sale
>>> Sale.objects.count()
```

### `filter`

```python
>>> from freegeek import Sale
>>> import datetime
>>> Sale.objects.filter(created_at__gt=datetime.datetime(2017,1,1)).count()
/home/hobs/.virtualenvs/freegeek/local/lib/python2.7/site-packages/django/db/models/fields/__init__.py:1474: RuntimeWarning: DateTimeField Sale.created_at received a naive datetime (2017-01-01 00:00:00) while time zone support is active.
  RuntimeWarning)
```

## Schemaless Django

### JSONField

Django has a JSONField that is kind-of like a  