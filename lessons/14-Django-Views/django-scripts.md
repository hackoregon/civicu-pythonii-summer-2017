# Python Scripts in Django

In django, if you want to run python code in a script that is not part of a Django project or app (called an "external script") you have to set some things up.
Django needs to know what settings module you want to use (what django project or site to import the settings.py from).
From there it can figure out what other Django apps it needs to read up on to find all their templates, views, urls, models, settings, etc.

There are several ways to run a script so that Django can do all this:

1. Launch `python manage.py shell` and then paste or import your script/functions from there.
2. Launch `python manage.py shell_plus` and use the `ipython` (`jupyter`) REPL (console) magic to `%run` your script
3. Pipe your script into `python manage.py shell` (FYI, this is also a great way to run SQL on your database, just pipe your SQL into `manage.py dbshell` instead of the `manage.py shell`)
4. Set your DJANGO_SETTINGS_MODULE environment variable and run django.setup() in your script.
5. Write a `manage.py` command of your own and add them to a pip-installable (like all those that django_extensions adds to django)!

## 1. `python manage.py shell`

## 2. `%run`

## 3. Pipe *.py into `python manage.py shell`

```bash
cat bot.py | python manage.py shell
```

You can see that there's one problem with this.
There's no way to easily pass command line arguments to your script, and our bot.py script needs those to be able to do anything interesting.
That's why we didn't use this method for our `bot.py` script.

### 3.b. Pipe *.sql into `python manage.py dbshell`

This works for SQL when you need to manually alter your database, install postgres plugins, etc.
This allows you to use the DB credentials stored in django to access your database, so you don't have to remember your password, port number, etc.
It also helps to make sure you're connecting to the same exact database that your django app is using.

## 4 `django.setup()`

This is what we did in [`bot.py`](https://github.com/totalgood/civicu_app/blob/master/labeler_site/bot.py) as well as in our [`image_info.py`](image_info.py) script.
This approach gives you the most flexbility and allows you to install your script in any package or directory (as long as it has access to a django project directory).

```python
import os
import django
from django.conf import settings  # Django magic starts here

# `labeler_site` must be a python package installed in your environment (virtualenv)
# OR "install" it manually before running this: `export PYTHONPATH=$PYTHONPATH:/path/to/labeler_site_basedir/`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labeler_site.settings')
django.setup()
```

## 5 Write an "Official" Django Manage Command!
