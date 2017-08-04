# Django Tutorial Challenge

## Add a form to upload a file

This blog post shows the right way to build a form so our users can upload new files to add to our directory containing images of animals (or just trees).

[Python Django Image Files Uploading Example](http://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php)

*OR* a simpler, more modern approach that uses templates (.HTML files a templates folder):

[How to Upload Files With Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

See if you can get something like this working in your app.
Consult the blog post above for steps 2-5 below.

1. Finish the [Django Tutorial part 2] to get `runserver` working, showing your Django Admin page for your project (the website your laptop serves up with `runserver`)
2. Add a Django Form to your Django app (not the project folder, the app folder): the form that takes a path to an image on the user's computer and submits a POST request back to your server
3. Implement a FileField in your Django models and link it up to the form you built in 2
4. Add a url path to your urls.py (it's better in your app rather than your project, but either is fine).
5. Get `python manage.py runserver` working and the form displaying on your laptop at `http://localhost:8000` + the URL path you put in `urls.py`
6. Download [this file](https://github.com/totalgood/civicu_app/blob/master/labeler/data/HUNT0133.jpg) to your `Desktop/` directory
7. Upload that file to your Django site using the form you built in #2 (doing something like `$ python manage.py runserver &; firefox http://localhost:8000/labeler`)
8. In class I'll ask you what the path is to this photo on your computer and what label (animal species or None) users should give it to "win"?
9. Completely Optional inspiration: visit [Powell's downtown at 7:30 for an author presentation](http://www.powells.com/book/wolf-nation-9780306824937/68-380)

``


## `labeler.forms.py`

My form has just a single field for the user to select or input a file path, but be careful about the names of the args to the Form instantiation so that they match up with your models.py name for the `FileField`

```python
from django import forms
from .models import Image


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', 'caption', 'uploaded_by')
```

## `labeler.views.py`

I modified the views in the `FileField` blog post above (the second simpler one with the ModelForm).
I looked for any mentions of that "docfile" or "document" other variables and strings used in the `forms.py` or `models.py` from the blog post.
I replaced them with *my* version of those field names for the labeler app.


```python
from django.shortcuts import render, redirect
from .models import Image
from .forms import FileUploadForm


def form_file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    return render(request, 'labeler/form_file_upload.html', {
        'form': form
    })
```

I left the `index()` view from the original Django tutorial, so I can have a "landing page" that can list the images if I like.
Eventually, I can add a link to the form and the "game" there.

Also, I replaced `documents` variable name and `Document` Model name with my `image` and `Image` names.
Be careful about this.
When you first try to run someone else's code (something you copy-pasted from a blog like this), make as few changes as possible to variable names.
Run it first and see where it breaks and fix the names one at a time.
And don't "fix" variable/class/function names if it works before the change!


```python
def index(request):
    images = Image.objects.all()
    return render(request, 'labeler/index.html', {'images': images})
```


## `labeler/templates/labeler/*.html`

You need to create a nested labeler directory within a new templates directory so that Django's template rendering engine finds it where it expects it.
The double-nesting of `labeler` is so that our Django app can be installed along side other apps, just like all those other packages your see on djangopackages.com.

This is where we'll put some `HTML` when we want to make this a prettier, funner game (or if we get tired of putting long, hard-coded `HTML` strings in our `views.py`).

### form_file_upload.html

```html
{% extends 'base.html' %}

{% block content %}
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
  </form>

  <p><a href="{% url 'index' %}">Return to Image List</a></p>
{% endblock %}
```

### form_file_upload.html

I've used HTML `<table>` tags to make my listing of files a bit neater than in the blog post.

```index.html
{% extends 'base.html' %}

{% block content %}
  <h3>Images</h3>
  <table>
    <tr><th>Filename</th><th>Uploaded</th></tr>
    {% for img in images %}
        <tr>
          <td><a href="{{ obj.file.url }}">{{ img.file.name }}</a></td>
          <td><small>{{ img.uploaded_date }}</small></td>
        </tr>
    {% endfor %}
  </table>
  <h3><a href="{% url 'form_file_upload' %}">Upload an image...</a></h3>

{% endblock %}
```


## `labeler/urls.py`

We need to connect our FileUploadForm view to a url before our browser can reach it with a GET request.

Your labeler/urls.py should be `include`d in the project's `labeler_site/labeler_site/urls.py`.

### `labeler_site/labeler_site/urls.py`

```python 
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^labeler/', include('labeler.urls')),
    url(r'^admin/', admin.site.urls),
]
```

### `labeler_site/labeler/urls.py`

The first url below will render the page at 'localhost/labeler/'.
The second one is for 'labeler/upload/'.

```python
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.form_file_upload, name='form_file_upload'),
]


If you need a little more help, a working version of this app is available at `http://github.com/totalgood/civicu_app`.