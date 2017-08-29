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

```python
>>> import doctest
>>> from labeler_site import bot
>>> doctest.testmod(bot)
```

How would you do this inside of a `TestCase`?
What are the return values for `doctest.testmod`?
Could you have an `assert` or `assertEqual` in your `TestCase`?

## `coverage` with [coveralls.io](http://coveralls.io) 

The python package coverage allows you to see how many of your lines of code are run during your tests!
This can provide you with a detailed report of your "test coverage" and give you ideas for more tests to run.
And if you hook coveralls.io up to your app you can add a badge to your github README.md so that you can "reward yourself" for increased coverage.

## Codecov 

[Codecov.io](http://codecov.io) is another service and python tool for visualizing code coverage with beautiful charts instead of those boring tables.
And there are badges for your readme too!

You can generate coverage reports using your `.travs.yml` and `pip install codecov` for any python package (django or otherwise).

So add `codecov` to your `test-requirements.txt`.

```text
# Add requirements only needed for your unittests and during development here.
# They will be installed automatically when running `python setup.py test`.
# ATTENTION: Don't remove pytest-cov and pytest as they are needed for `python setup.py test`.
pytest-cov
pytest
coverage
codecov
doctest2
```

And make sure your `test-requirements.txt` are installed on travis by adding them to your `.travis.yml` under the `install:` key.
Since codecov will be installed you can add it to the `after_success:` key so that it generates a coverage report each time your tests pass.
This report will be uploaded to [codecov.io](codecov.io) once you have linked it to your `github.com` account.

```yaml
sudo: false
language: python
virtualenv:
  system_site_packages: false
env:
  matrix:
    # - DISTRIB="ubuntu" PYTHON_VERSION="2.7" COVERAGE="true"
    # - DISTRIB="conda" PYTHON_VERSION="2.7" COVERAGE="false"
    # - DISTRIB="conda" PYTHON_VERSION="3.3" COVERAGE="false"
    # - DISTRIB="conda" PYTHON_VERSION="3.5" COVERAGE="false"
    - DISTRIB="ubuntu" PYTHON_VERSION="3.5" COVERAGE="false"
addons:
  apt:
    packages:
      - git
      - python-pip
install:
  # - source tests/travis_install.sh
  - pip install --upgrade pip
  - pip install -r requirements.txt
  - pip install -r test-requirements.txt    # THIS INSTALL CODECOV, etc.
before_script:
  - git config --global user.email "travis.github@totalgood.com"
  - git config --global user.name "Travis Testing for Total Good civicu_app"
script:
  - python manage.py test
  - python setup.py test
after_success:
  - codecov  # THIS WILL UPLOAD COVERAGE REPORT TO codecov.io
  - if [[ "$COVERAGE" == "true" ]]; then coveralls || echo "failed"; fi
cache:
  - apt
```

Your codecov token can be found at `codecov.io/gh/your_github_account_name/your_repository_name`.
For example mine is at [https://codecov.io/gh/totalgood/civicu_app](https://codecov.io/gh/totalgood/civicu_app)

You can set the token in your local environment (on your laptop) with:

```bash
export CODECOV_TOKEN="19abc123-hex8-9876-a881-8412af152dc0"  # USE *YOUR* TOKEN
```

And you can add your codecov "Upload Token" to the [travis-ci](http://travis-ci.org) settings for your repo.
Click on the "More Options" button in the upper right for the travis-ci page for your repo.
Select the "Settings" gear menu item.
Scroll down the setting until you find "Environment Variables".
The environment variable name is `CODECOV_TOKEN` and the "value" is your "Upload Token" from your codecov.io accounts page.


Or you can run `codecov` manually with

```bash
codecov --token=19abc123-hex8-9876-a881-8412af152dc0
```

If you've `export`ed your environment variable on your laptop in your bash.rc file or somewhere that always runs when you log in, you don't have to provide the `--token`.


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
- add a badge (URL to an image) for your Travis test fail/success 

##### Add a Badge

Hack your travis url to find an image that is green when your tests pass.
Mine was here: `https://travis-ci.org/totalgood/civicu_app.svg`.
And my travis page for reviewing the `builds` for that app was here: `https://travis-ci.org/totalgood/civicu_app/`.

So this markdown creates an image on my github profile page for my `civicu_app` that tells me when your tests pass:

```markdown
+[![Build Status](https://travis-ci.org/totalgood/civicu_app.svg?branch=master)](https://travis-ci.org/totalgood/civicu_app/)
```

Now my development workflow is "gamified".
Like a linter, this encourages me to do things right... to not break my tests and write correct code.
