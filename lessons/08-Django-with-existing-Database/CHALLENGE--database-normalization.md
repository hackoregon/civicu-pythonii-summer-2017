# Database Challenge

## Database Normalization

Find one or more fields in Free Geek's massively denormalized schema that can be normalized. Try to find one that we did not find during class.

1. What fields would you add or delete
2. What tables would you add or delete
3. What relationships would you add or delete
4. Pseudo-code your changes in a `models.py` file, with field type, ForeignKey target names, and primary keys explicitly defined
5. Put your answers to 1-3 in the docstring of your `models.py` file
6. Push your `models.py` file to your `civicu-pythonii-summer-2017/student-work/your-name/` folder
7. PR your student-work folder to the [hackoregon](https://github.com/hackoregon/civicu-pythonii-summer-2017/tree/master/student-work) repo

### Free Geek database schema

#### `models.py`

Created using `python manage.py inspectdb` from within the free-geek project which has `settings.DATABASES['default']` pointing to the existing Free Geek ruby app's database.

Noticed the `Meta:` class at the bottom. What do you think that does?


#### Entity Relationship Model (ERM)

An [ERM](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) is a diagram of all the tables and fields in those tables and their relationships to one another. If you install `django-extensions` and add it to your `INSTALLED_APPS` you can create one from any set of Django models (a `models.py` file).

```bash
$ python manage.py graph_models
```

Here's the ERM for Free Geek's legacy database:

![Free Geek's previous database schema diagram with > 200 tables](https://github.com/codeforgoodconf/free-geek/blob/master/docs/previous_schema.png ERM for Free Geek's legacy database)








