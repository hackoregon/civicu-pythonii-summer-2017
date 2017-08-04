# Leson 6: Your First Django App

## Review

OK, we've learned a lot over the past few days.

We know how to ...

- read and write files (especially CSV files)
- issue GET requests to websites
- retrieve json data from APIs and decode it into Python objects
- put up a scaffolding (boilerplate, best practices code) for any project, like a console script or a Django app
- install our python app so our console scripts are callable from any directory
- gather up all our installed packages into a virtualenv
- we know how to write docstrings (later we'll learn how to turn those into docs)
- we know how to write and run tests

## Errata

- An HTTP GET request only requires a path, not necessarily query parameters like `?page=1`
- Only an API request (usually a REST request) requires query parameters with `?` and `=` symbols
- When I finally installed a linter in my fresh sublime install, it flagged my poor use of == True
- Watch out for NaNs too, they're even more mysterious

Here's the `==` vs `is` confusion. But it makes logical sense, if you think hard about it, because of the "readability" of python and what the meaning of the word "is" is ;)

```python
>>> None is False
False
>>> None == False
False
>>> 0 == False
True
>>> 0 is False
False
>>> hist -o -p
```

Here's some even more confusing properties about NaN's. This is because Python (and most other languages) comply with IEEE floating point math, which includes rules for handling NaNs and +INFs and -INFs.

```python
>>> np.nan == float('nan')
False
>>> np.nan is float('nan')
False
>>> float('nan')
nan
>>> np.nan
nan
>>> np.nan > 0
False
>>> np.nan <= 0
False
>>> np.nan == 0
False
>>> np.nan != 0
True
>>> np.nan != np.nan
True
>>> np.nan != float('nan')
True
>>> np.nan == np.nan
False
>>> np.nan != np.nan
True
>>> float('nan') != float('nan')
True
>>> float('nan') == float('nan')
False
```

So a `nan` is not equal to or greater than or less than anything, not even itself.
That's because a `nan` is not a number, not a value, not anything that can be equal to or greater than any other value or number.

What about `inf`inity?

```python
>>> np.inf > 0
True
>>> np.inf > np.nan
False
>>> np.inf < np.nan
False
>>> np.inf <= np.nan
False
>>> np.inf != np.nan
True
>>> hist -o -p
```

also

```bash
$ git status --ignored

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

  modified:   lessons/06-Django-MTV/README.md

Ignored files:
  (use "git add -f <file>..." to include in what will be committed)

  .ipynb_checkpoints/
  exercism-linux-64bit.tgz
  homeless.csv
  lessons/.ipynb_checkpoints/
  lessons/03-HTTP-and-APIs/homeless.csv
  lessons/shared-resources/flake8.cfg
  lessons/shared-resources/food-carbon-footprint.csv
```

## My Answer to the Challenge

First I noticed that my environment wasn't correcting my syntax and style errors, so I installed a new linter.
And it turns out there's a much better plugin for *Sublime Text 3* than flake8!!!
Unfortunately it's called *Anaconda*, but it's different from the `conda` package manager that you're used to on Windows.

I've corrected the tests to use `is` rather than `==` as a result of the linter nags.

And I'm adding some git hooks to stop me from editing files in the build and egg directories and cluttering up my global `find` or `ctrl-p` in *Sublime*.

## *Retro*spective

Let's pair up when we have bugs to fix so we can parallelize the fixing of them. ;)

## The Official Django Tutorial

Now let's learn how to build a web application using the Django framework.

Let's start making use of that boilerplate Django app that PyScaffold `putup` for us.
We'll the official [Django tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) pretty closely.
Today we'll finish the first two sections of the tutorial, which should get us halfway through the app.

1. [Part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
2. [Part 2](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)

## Our Design

But our app is going to do something for Hack Oregon so it can be part of the Civic PDX platform if we do a good job.
And it's going to be a game!
We're going to gamify data entry!

A lot of Data Science and Machine Learning problems require labeled data, data that is labeled with the "right answer".
Like recognizing images of cats and dogs with neural nets requires a lot of pictures of cats and dogs that have been "labeled" with the right answer.
Just like a human, machines need examples with the "right answer" to learn from.

- To recognize spam or trolling you need to label obnoxious text from twitter or reddit as well as nice polite tweets and posts
- To recognize endangered species "caught on hidden camera" you need labeled pictures of endangered species like wolves, wolverines and foxes as well as nonindenagered species like bear and elk  
- To recognize students walking in front of your webcam you label images with the correct name of the student

Reading and labeling trolly tweets would be kind of hard to "gamify" and make fun.
But labeling cats and dogs (or Mountain Lions and Wolves), no that could be fun.
It'll be like a "where's waldo" game!

So the ["Your First Django App" tutorial on the DjangoProject website]. But our web app is going to be a game for classifying data. It will help us classify building construction data, automotive accident data, wildlife camera picture data, and even astronomical pictures of Black Holes. We'll get this data like from the city of Portland through the CivicPDX platform API or directly from local nonprofit organizations like Cascadia Wild (images of endangered carnivores like Wolverines on Mt Hood).

Here's a list of some of our User account maintenance features our app will have

1. A "landing page"
1. User self-registration
2. Login
3. Logout
4. User profiles with full name, and e-mail (used for the username)

We'll actually save all that for when we actually have users and can put our app on a public server.
So for now we'll focus on the game part of the app.

1. Display an image
2. Display a caption for the image (at first just the file path)
3. A radio button or pulldown to select a label for the image displayed
4. A record of the answer and how long it took the "player" to label the image
5. An optional text field for the user to enter a comment about the image or their label

### Docs First

Let's take a moment to write something up in the README.md file about your picture labeling game.
Our package already contains the boilerplate for our app, we just need to fill in the blanks.

### Django

Make sure django is installed within your virtualenv

```bash
$ source ~/.virtualenvs/labelerenv/bin/activate
```

*OR*

```bash
$ workon labelerenv
```

*THEN*

```bash
$ pip install django
$ python -m django --version
1.11.3
$ python -c "import django; print(django.__version__)"
1.11.3
$ django-admin --version
1.11.3
```

### `django-admin startproject`

If you used putup to start your package, you should already have a manage.py file as well as settings.py and urls.py in your package directory somwhere.
So you can skip that step in the Django tutorial.
Just keep in mind that a Django project is kept within a Python package.
When the tutorial talks about you naming the outer `mysite` folder anything you like, that's the folder I called "labeler_site."
That's the name I put in at the end of the `putup` command.
And putup assumed that my Django project would have the same name, so there's an inner folder called "labeler_site" where the tutorial has it as `mysite`.

### `django-admin startapp`

Now we're going to add a Django app along side our Django project. Our Django project will take care of things like users and a home page. The Django app will take care of only one thing, the pages associated with the image labeling game.
A good Django app focuses on one thing and tries to do that one thing well.

```bash
$ cd ~/src/labeler_site/
$ django-admin startapp labelgame
```

## `settings.py`

If you're having trouble setting the TIMEZONE setting, check out this [blog post](https://tommikaikkonen.github.io/timezones/).
Hint: search for "America" on that page and you may find a city name for a time zone that's the official `pytz` name for `PDT` or `PST`.
Second hint: It's not `'Portland'` or `'PDX'` or `'PDT'` or `'PST'` ;)

Also, most settings should be single-quoted strings if you want to have beautiful code that is consistent with the style of some of the best python developers I know.
They use single quotes for any string that is designed to be read by a machine, like settings and configuration parameters and dictionary keys. These strings would break something if they were off by a single character, even whitespace.
That way you can use double-quotes to identify human-readable strings that are typically much longer and don't affect how your app runs, just what it displays to your user or developers exercising its internal or public APIs.
This convention will make it really easy to search-replace all those double quotes with a `gettext()` function call if you ever want to localize your app (translate all those human-readable strings into another language).

## `labelgame.models.py`

My `models.py` looks something like this (in the database class Mark will show you how to "normalize" away that third `Model` to simplify this data schema):


```python
class Image(models.Model):
    filepath = models.CharField("Path relative to BASE_PATH for the image file",
                                max_length=512)
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512)
    created_date = models.DateTimeField('Date photo was taken.')
    file = models.FileField(upload_to='.')


class UserLabel(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)


class TotalVotes(models.Model):
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
```


## `labelgame.forms.py`

My form has just a single field for the user to select or input a file path, but be careful about the names of the args to the Form instantiation so that they match up with your models.py name for the `FileField`

```python
from django import forms


class ImageUploadForm(forms.Form):
    imagefile = forms.FileField(
        label='Select an image file',
    )
```

## `labelgame.views.py`

I copy-pasted this from the `FileField` blog post above and then looked for any mentions of that "docfile" or other variables and strings used in the `forms.py` or `models.py` from the blog post.
I replaced them with *my* version of those field names for the labelgame app.

```python
from .models import Image
from .forms import ImageUploadForm


def list(request):
    # Handle imagefile upload
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimage = Image(file=request.FILES['imagefile'])
            newimage.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = ImageUploadForm()  # An empty, unbound form

    # Load images for the list page
    images = Image.objects.all()  # noqa

    # Render list page with the images and the form
    return render_to_response(
        'myapp/list.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )
```

Of course, I left the `index()` view from the original Django tutorial, so I can have a "home page" that works too. Eventually, I can add a link to the form there.

Also, I replaced `documents` variable name and `Document` Model name with my `image` and `Image` names.
Be careful about this.
When you first try to run someone else's code (something you copy-pasted from a blog like this), make as few changes as possible to variable names.
Run it first and see where it breaks and fix the names one at a time.
And don't "fix" variable/class/function names if it works before the change!


```python
def index(request):
    return HttpResponse("This the home page of the Wolf Labeler App.")
```

## `labelgame/templates/labelgame/*.html`

This is where we'll put some `HTML` when we want to make this a prettier, funner game (or if we get tired of putting long, hard-coded `HTML` strings in our `views.py`).
