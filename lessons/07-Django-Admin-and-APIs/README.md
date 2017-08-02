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
