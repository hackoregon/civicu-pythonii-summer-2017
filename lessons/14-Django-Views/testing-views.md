# Testing Views

We're going to use the best-practices described in the [django documentation](http://django-testing-docs.readthedocs.io/en/latest/views.html) to test our `labeler` apps views and improve our test coverage.

## Django Client

Django ships with a python client that acts like a browser.
It's like the `requests` package that we used to exercise our API, but it has request and response objects that are identical to what a Django views would use.

However, we're going to implement these tests in docstrings.
The only disadvantage to using doctests (in docstrings) is that it makes it more difficult to see the output tracebacks when tests fail.
And it's a bit tricker to set breakpoints with `pdb` (the python debugger).
But since we aren't using the debugger, and we can write our tests to make sure the tracebacks are provided, I think doctests are a better way to go.

```python
>>> from django.test import Client
>>> from labeler.models import Image, Label, UserLabel
>>> import datetime
>>> from django.core.urlresolvers import reverse

>>> client = Client()

>>> response = client.get(reverse('blog_index'))
>>> response.status_code
200
>>> response = client.get(reverse('blog_category_list'))
>>> response.status_code
200
>>> category = Category(title='Django', slug='django')

>>> category.save()
>>> response = client.get(category.get_absolute_url())
>>> response.status_code
200

>>> post = Post(title='My post', slug='my-post', body='Lorem ipsum
dolor sit amet', status=2, publish=datetime.datetime.now())
>>> post.save()
>>> post.categories.add(category)


>>> response = client.get(post.get_absolute_url())
>>> response.status_code
200
"""

