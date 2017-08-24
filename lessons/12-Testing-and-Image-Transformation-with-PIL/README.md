# Testing

## Django Unittests

- data fixtures
- testing models
- testing views
- testing templates
- testing APIs

### Fixtures

Many functions (units) in a Django app require access to data.
But the test environment (your laptop or Travis) usually does not have the entire database.
And we often don't want to mirror our database in many places for security and privacy reasons.
So we need to be able to create fixtures of small portions of your database that can be loaded quickly for each test.

Each function (each unittest) needs a fresh, reliable, consistent set of data, so the tests can predict what the output should always be.

We can create a json dump of our exising data using the `dumpdata` manage.py command:

```bash
python manage.py dumpdata labeler > labeler/fixtures/labeler_test_data.json
```

If you need to "anonymize" your production data, for privacy or security, you can load and modify the data with `json.load()` and `json.dump()` just like any other json file or string.
Or if the dump is really small, you can just edit it in your text editor (after setting the `indent=2` kwarg in json dump so it is easier to read).

You also need to tell django where your fixtures are stored by adding something like this to your `settings.py` file.

```
FIXTURE_DIRS = ('labeler/fixtures/',)
```

Your `python manage.py test` will load fixtures from that folder only if you tell it to.
So after you derive your test class from the  

And then

This will dump your apps data to a json file under the fixtures directory in your app. Other available formats are .xml and .yaml (see https://docs.djangoproject.com/en/1.8/ref/django-admin/#dumpdata-app-label-app-label-app-label-modelfor more options).

In your settings.py file you will need to tell django about where your fixtures reside like this:

FIXTURE_DIRS = (‘APP_NAME/fixtures/’)
```

## Doctests

Doctests are great for both showing other developers how to use your code.
One example is often worth a thousand words.

Doctests are horrible for functions that output strings and need to be both python2 and python3 compatible.
The problem is that `repr(unicode(''))` and `repr(str(''))` and `repr(bytes(''))` can be different on each.

Doctests are also bad for functions that return large complicated data structures, like dataframes.

So you still need unittests.
But with a few lines of code your unittests can be configured to *also* run doctests. 