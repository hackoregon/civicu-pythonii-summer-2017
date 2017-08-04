# Your first Djnago App!

Now we're going to take advantage of some magic built into Django.

## Django Admin Interface

The admin interface provides some pretty nice "CRUD" for any data in our system.

- *C*reate
- *R*ead
- *U*pdate
- *D*elete

Administrators need to be able to change any of the data that exists in our system.
They may want to correct or delete any wildlife labels that were posted accidentally or incorrectly.

## Django REST Framework (DRF)

A particularly awesome [django-package](http://djangopackages.com) called [DRF](http://www.django-rest-framework.org/tutorial/1-serialization/) makes it possible to build an API with only a few lines of code for each model (database table) you want to "expose" to the world.

### An Alternative to DRF

What about [API Star](https://github.com/tomchristie/apistar)? For a production API on a website with a lot of traffic and a lot of developers trying to get to your data, API Star is definitely the way to go. It produces documentation and client libraries (in both Python and Javascript) that stay in sync with your API as it evolves.  And it will work with other database ORMs besides django (like SQL Alchemy which is often used in Flask). But it wouldn't give you much insight into Django or how APIs work. And 

### Explore DRF

#### A Working DRF API

Here's a [working app](https://totalgood.org/bicycle/) that uses DRF to generate the API for Zak's bike theft-rate tool.

Spend the next 10 minutes exploring it (both with requests and your browser).

1. Try to find the theft rate score for the bike rack outside PNCA.
2. Try to find a safer bike rack nearby.

#### The Anatomy of a DRF API

Here's the [source code](https://github.com/Zak-Kent/Bicycle_theft_API) for that bicycle theft rate API.

Spend the next 10 minutes tracing the flow of your API requests through the source code.
Your request goes through the `urls.py` first, which triggers a view, which may call a template, which will likely query a model (table in models.py).
This is in the reverse order of MTV, plus a U thrown in to connect the "plumbing."

*U*: Which `url_pattern` matched your requests?
*V*: Which view did your GET requests use?
*T*: Which templates did your request use to render the view?
*M*: Which model did your GET requests get their answer from?

### Design a DRF API

What do you think a developer might like to do programatically:

[x] upload an image
[x] download an image
[x] retrieve an individual "vote" (user id, image id, label str)
[x] retrieve the "correct" label for an image
[-] count the votes for each label for an image
[-] retrieve "crowd" label for an image

What endpoints do we need to make this possible?
Which tables are these going to query?

The first four of these are queries or insertions of a single row in a single table.
The bottomA couple of them are aggregations across many rows in a table.
For now we'll focus on the single-row endpoints.
Your client can then do any aggregations you like in python.
After the next lesson about Databases and Django's ORM you can implement customized "shortcut" endpoints for computing these totals or aggregations.

So our endpoints (views) for this lesson are going to be:

[x] `/api/image/` (GET to download an image)
[x] `/api/image/` (POST to upload an image)
[x] `/api/userlabel/` (GET a user's vote for an image label)
[x] `/api/truelabel/` (GET the true image label, if it is available)

### Let's Build It!




