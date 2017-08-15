# Your first Django API!

Now we're going to take advantage of some magic built into Django to build an "admin interface"

## Review

Demonstrate your implementation of a file upload form.

Show how to add an list template view of the images.

[my implementation](https://github.com/totalgood/civicu_app)


## Templates

Add picture display to the list view.

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
A couple of them are aggregations across many rows in a table.
For now we'll focus on the single-row endpoints.
Your client can then do any aggregations you like in python.
After the next lesson about Databases and Django's ORM you can implement customized "shortcut" endpoints for computing these totals or aggregations.

So our endpoints (views) for this lesson are going to be:

[x] `/api/image/` (GET to download an image)
[x] `/api/image/` (POST to upload an image)
[x] `/api/userlabel/` (GET a user's vote for an image label)
[x] `/api/truelabel/` (GET the true image label, if it is available)

### Let's Build It!

#### Serializers

Serializers turn a database table (or a set of records from a DB table) into a "serial" stream suitable for transmission over a serial interface (digital IO, serial port, USB, or Ethernet packet).

Deserializers turn a serialized string of ascii characters into a database record (or python data structure).

Can you think of any serializers or deserializers that we used during the class on HTTP GET requests where we downloaded data from a CivicU API?

Can you think of any other serialization formats? (hint, you can visit the Civic U api for the homeless project to get at least one more kind)?

Why do you think one format has become the most popular?

How would you serialize 3 database records from our app?

Isn't `print()` and `str()` a serializer?

#### A Serializer for our Fields

How would you serialize this data model (table)?

```python
class Image(models.Model):
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512, default=None, null=True)  # , required=False)
    created_date = models.DateTimeField('Date photo was uploaded.', auto_now_add=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)  # , required=False)
    file = models.FileField("Select file to upload", upload_to='images')
```

##### CharField

- Can you guess how to serialize a `CharField`?
- What does a CharField store? 
- What is a good `str` or serial representation of a `CharField`


##### ForeignKey

We have a foreign key to another model, `User`. How do we deal with that?

What is a good, unambiguous serial representation of a User instance in our DB?

How does our app *id*entify a particular user?

##### DateTimeField

How do you serialize a date?

Is it always deserializable?

How can we test a serializer for dates?

##### FileField

How can we represent a FileField?

What does the `str` representation of a FileField look like?

Is that good enough?

How is `FileField` like a `ForeignKey`?

Can we provide a representation that would allow the client to "dig deeper" if they wanted to, without slowing down the API response by sending them the entire image?

