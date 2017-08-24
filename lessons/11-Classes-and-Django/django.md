# Django MTV

## Data flow

```text
Client -> HTTP request [-> nginx/apache/whitenoise] -> gunicorn -> wsgi
(Browser)                                                             |
   ^                                                                  |
   |                                                                  v
   - HTTP response <- template.html <- models.py <- views.py <- urls.py
```

Another way to think about it

```text
database.sqlite3 -> models.py -> views.py -> template.html -> urls.py -> Browser
```

## Model

Models give you (and django) a pythonic way of defining the structure (schema) of your database and then accessing your data through an ORM (Object Relational Mapping = objects that represent data records from your database).

  - query for records (QuerySet)
  - create tables
  - modify tables without losing data from the existing tables
  - add records to your database tables
  - maintaining valid relationships between your tables (query validation)

## View

You need one view for each "kind" of page you want in your app.

- Home page (list of images in our DB?)
- Image "details" page, a form for viewing, changing, or uploading an Image
- Image upload page
- A way to label an image
- Display the aggregate (sum) of the label "votes" for an image
- List the individual votes for an Image 

## Template

A template holds all the HTML "around" the data that the view will insert into the template tags. It tells the browser *"how"* to display the data. The view just says *"what"* the data is.

## URL

A URL tells the server which view to use for a particular GET request.

## Let's Create a Class for Django Admin


```python
class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'taken_date'
    list_display = ('taken_date', 'created_date', 'file', 'caption', 'uploaded_by')


admin.site.register(Image, ImageAdmin)
```

What is the parent class of this Admin class?
What are the class attributes of this class?
What are the instance attributes of this class?
