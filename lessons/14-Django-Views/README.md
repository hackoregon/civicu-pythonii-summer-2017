# Django Views

1. Attendance
2. Exercisms
3. Using PIL to get Exif
4. ManyToManyField for Image labels (tags)
3. Django Views for `labeler` app
4. Testing Django Views
5. Review

## Excercisms 11 & 12

- exercism 11: [meetup](../../student-work/hobson_lane/exercism/python/meetup/README.md)
- exercism 12: [rotational-cipher](../../student-work/hobson_lane/exercism/python/rotational-cipher/README.md)

## ManyToManyField

Let's add a ManyToManyField to our models.
This will allow us (and our users) to add new labels and tag each image with multiple labels
## A View for User Labeling of Images

We'll write a new view (and a new form and template to go along with it) to allow users to label the images we upload to our labeler app through the API of the image upload form.

- [views.md](views.md)

## Testing Django Views

We'll write both doctests and TestCase classes for our new labeler app views.

- [testing.md](testing.md)

## [Review](review.md)

A brief review of this advanced Python course to help you prepare for the exam.

### Coursework

- build a django app and push it to `github`, with at least one doctest and one `TestCase`
- complete at least 10+2 exercisms with ~95% of tests passing

### Code Challenges

The 3 code challenges may involve use of:

- `zip` and `zip(*...)`
- `*.csv` files
- `requests`
- `with`, `open()`, `.close()`, `.read()`, `.readline()`
- `dict`, `defaultdict`, `namedtuple`, `Counter`, `list`, `tuple`, `bool` coercion
- `str`, `unicode`, `encode`, `decode`, `str.join()`, `str.split()` 
- `class`, `def`, `__init__()`, `__repr__()`, `__str__()`, `__len__()`, `__dict__()` 

### Multiple Choice Questions

The 10+2 multiple choice questions each may have multiple answers.

### Outside Help (Resources)

You can use help from within your python or ipython or jupyter or anaconda environments, or any of the files and documentation found in the github repos `github.com/totalgood/civicu_app` and `github.com/hackoregon/civicu-pythonii-summer-2017` or any repos you have ever created, cloned, or pushed to on github. You may also install any packages from pypi using `pip` or `conda` and the documentation those packages contain and any documentation you can find on [readthedocs.org](https://readthedocs.org/), built by a local Portland python hero, [Eric Holscher](http://ericholscher.com/blog/2012/jan/22/why-read-docs-matters/).








