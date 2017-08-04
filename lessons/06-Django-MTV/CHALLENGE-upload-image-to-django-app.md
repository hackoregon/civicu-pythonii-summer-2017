# Django Tutorial Challenge

## Add a form to upload a file

This blog post shows the right way to build a form so our users can upload new files to add to our directory containing images of animals (or just trees).

[Python_Django_Image_Files_Uploading_Example](http://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php)

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

