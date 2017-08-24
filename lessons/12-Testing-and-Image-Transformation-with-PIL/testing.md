# Testing

- Django
- Continuous Integration (CI)
- Integration Tests

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
mkdir labeler/fixtures
python manage.py dumpdata --indent=2 labeler > labeler/fixtures/labeler_test_data.json
```

If you need to "anonymize" your production data, for privacy or security, you can load and modify the data with `json.load()` and `json.dump()` just like any other json file or string.

Or if the dump is really small, you can just edit it in your text editor (after setting the `indent=2` kwarg in `json.dump(**kwargs)` so it is easier to read).

You also need to tell django where your fixtures are stored by adding something like this to your `settings.py` file.

```
FIXTURE_DIRS = ('labeler/fixtures/',)
```

Your `python manage.py test` will load fixtures from that folder only if you tell it to.

So after you derive your test class from the 

And then

This will dump your apps data to a json file under the fixtures directory in your app. Other available formats are .xml and .yaml (see https://docs.djangoproject.com/en/1.8/ref/django-admin/#dumpdata-app-label-app-label-app-label-modelfor more options).

In your tests.py file you will need to tell your tests to load the fixture:

```
import labeler_site.settings
from .models import Image
# from .forms import FileUploadForm

MEDIA_ROOT = labeler_site.settings.MEDIA_ROOT


class ImageModelTest(TestCase):
    fixtures = ['labeler_test_data.json']
```

And you'll want to create this fixtures

## Doctests

Doctests are great for both showing other developers how to use your code.
One example is often worth a thousand words.

Doctests are horrible for functions that output strings and need to be both python2 and python3 compatible.
The problem is that `repr(unicode(''))` and `repr(str(''))` and `repr(bytes(''))` can be different on each.

Doctests are also bad for functions that return large complicated data structures, like dataframes.

So you still need unittests.
But with a few lines of code your unittests can be configured to *also* run doctests. 

## Coverage and Coveralls.io

The python package coverage allows you to see how many of your lines of code are run during your tests!
This can provide you with a detailed report of your "test coverage" and give you ideas for more tests to run.
And if you hook coveralls.io up to your app you can add a badge to your github README.md so that you can "reward yourself" for increased coverage.

## Continuous integration

Continuous integration is when you allow your code to be deployed or integrated without any manual human QA testing.
To make this happen you need to have a lot of test coverage and have high confidence in your code review and testing process.
And you need to automate the test running with a tool like travis.
Travis also allows you to add a badge to your README.md that will reward your developers (yourself) when tests are passing on `master` and/or `develop` branches.

### Git Workflow for CI

Best practice work flow is to have master tests always passing and allow `develop` tests to fail, but try hard to correct them quickly.
Only feature branches should have failing tests pretty much perpetually.

```bash
git checkout develop -b feature/123-add-image-upload-api
# document the new feature and commit that
python manage.py test  # tests should pass
# add tests for the new feature
python manage.py test  # tests should fail 
# implement the feature, then...
python manage.py test  # tests might fail many times
# keep working until the tests pass on your feature branch, then...
git pull origin develop  # merge in the latest from your team
python manage.py test  # fix broken tests
git checkout develop 
git pull  # need to pull your fellow developers latest changes
git merge feature/123-add-image-upload-api
python manage.py test  # these should pass, if not, fix
git push origin develop
```

Each time you push to your feature branch or develop, Travis runs tests for you.
So if you forget, or just want to keep hacking, you can check Travis's test results rather than running them on your local environment.
Sometimes tests will pass on Travis and not locally, or vice versa, if there are environment differences (usually different data in the database).
The merge to develop can also be done as a code-reviewed PR, if that's what your boss wants.
Code reviews can also happen when you issue a PR to master from develop.

### Travis

#### In-Class Workshop

- Sign up for a free Travis account
- edit the .travis.yml file
