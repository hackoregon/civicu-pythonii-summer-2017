# Your First Django App

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
$ source ~/.virtualenvs/civicu_app_env/bin/activate
```

*OR*

```bash
$ workon civicu_app_env
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
When the tutorial talks about you naming the outer `mysite` folder anything you like, that's the folder I called "civicu_app."
That's the name I put in at the end of the `putup` command.
And putup assumed that my Django project would have the same name, so there's an inner folder called "civicu_app" where the tutorial has it as `mysite`.

### `django-admin startapp`

Now we're going to add a Django app along side our Django project. Our Django project will take care of things like users and a home page. The Django app will take care of only one thing, the pages associated with the image labeling game.
A good Django app focuses on one thing and tries to do that one thing well.

```bash
$ cd ~/src/civicu_app/
$ django-admin startapp labelgame
```

## Model

## View

## Template

