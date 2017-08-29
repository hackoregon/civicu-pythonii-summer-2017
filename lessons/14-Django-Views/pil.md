# Image Manipulation with PIL

PIL (`pip install pillow`) is great for manipulating images.
Some alternatives include:

- [`Image Magick`](http://www.imagemagick.org/script/index.php) ([`PythonMagick`](http://www.imagemagick.org/download/python/)) or [MagickPy](https://pypi.python.org/pypi/MagickPy) with `pip install MagickPy`
- [`PyOpenCV`](https://pypi.python.org/pypi/opencv-python) with `pip install opencv-python` or `pip install opencv-contrib-python`
- Python scripting in GIMP (opensource PhotoShop)!

We're going to use `PIL` in our labeler app to extract the metadata (Exif headers) from JPG and TIFF image files. 

## Exif

[Exif](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) or "Exchangeable image file format" is the standard way to store data in an image file.
In *Exif* the pixels are kept separate from metadata like focal length, lat/lon, camera make and model, and any comments or captions a user might have added to an image.
But manufacturers play fast and loose with this standard making it difficult to predict exactly which fields will be populated and how to decode them.
This is good and bad, it makes it hard to develop software to take advantage of it, but it also makes it hard to reverse engineer and forge all of this header information.
This is one of the ways they detect forged images coming out of North Korea or other "fake news" sources.
Nonetheless, the PIL package in python can read these fields from most images and audio files where it is available as part of the file format specification (JPEG, TIFF, WAV)

Make sure you have `pillow` (PIL) installed and it's in your requirements.txt (in your labeler app).

```bash
pip install pillow
# if the line above said it was already installed (probably with `django_extensions`) then you don't need to do this:
pip freeze | grep -i 'pillow==' >> requirements.txt
```

Lets set this up as an [external Django script](django-scripts.md) so we can use BASE_DIR to find wolf photos in our labeler app:

```python
import os

import django
from django.conf import settings  # noqa Django magic starts here

import PIL.Image
from pprint import pprint

# `labeler_site` must be a python package installed in your environment (virtualenv)
# OR "install" it manually before running this: `export PYTHONPATH=$PYTHONPATH:/path/to/labeler_site_basedir/`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labeler_site.settings')
django.setup()
```

Now that we've got settings for our app and PIL we can use it to extract the EXIF header from a jpg of a wolf:


Now we can import `PIL` and mess with our images:


```python
img = PIL.Image.open(os.path.join(settings.BASE_DIR, 'labeler', 'data', 'SUNP0254.jpg'))
exif_data = img._getexif()
```

But that `exif_data` `dict` is not super-helpful:

```python
>>> pprint(exif_data)
{271: 'Icatch',
 272: 'WF121',
 282: (240, 1),
 283: (240, 1),
 296: 2,
 305: 'Adobe Photoshop Lightroom 4.4 (Windows)',
 306: '2016:07:31 14:16:14',
 33434: (1, 60),
 33437: (32, 10),
 34665: 200,
 34850: 2,
 34855: 100,
 36864: b'0230',
 36867: '2014:04:27 17:40:29',
 36868: '2014:04:27 17:40:29',
 37377: (5906891, 1000000),
 37378: (3356144, 1000000),
 37379: (-5000, 1000),
 37380: (0, 10),
 37381: (3, 2),
 37383: 4,
 37384: 0,
 37385: 1,
 37386: (82, 11),
 37396: (1536, 1152, 3072, 2304),
 41728: b'\x03',
 41729: b'\x01',
 41985: 0,
 41986: 0,
 41987: 0,
 41988: (0, 1),
 41990: 0,
 41991: 0,
 41992: 0,
 41993: 0,
 41994: 0,
 41996: 0}
```

Fortunately PIL comes with an answer key we can use to clean up that dictionary.

```python
>>> from PIL.ExifTags import TAGS as tag_num2name
>>> dict(zip(map(tag_num2name.get, exif_data.keys()), exif_data.values()))
{'ApertureValue': (3356144, 1000000),
 'BrightnessValue': (-5000, 1000),
 'Contrast': 0,
 'CustomRendered': 0,
 'DateTime': '2016:07:31 14:12:50',
 'DateTimeDigitized': '2016:06:24 18:08:29',
 'DateTimeOriginal': '2016:06:24 18:08:29',
 'DigitalZoomRatio': (0, 1),
 'ExifOffset': 206,
 'ExifVersion': b'0230',
 'ExposureBiasValue': (0, 10),
 'ExposureMode': 0,
 'ExposureProgram': 2,
 'ExposureTime': (1, 310),
 'FNumber': (32, 10),
 'FileSource': b'\x03',
 'Flash': 1,
 'FocalLength': (82, 11),
 'GainControl': 0,
 'ISOSpeedRatings': 100,
 'LightSource': 0,
 'Make': 'BUSHNELL',
 'MaxApertureValue': (3, 2),
 'MeteringMode': 4,
 'Model': '119533CW',
 'ResolutionUnit': 2,
 'Saturation': 0,
 'SceneCaptureType': 0,
 'SceneType': b'\x01',
 'Sharpness': 0,
 'ShutterSpeedValue': (8276124, 1000000),
 'Software': 'Adobe Photoshop Lightroom 4.4 (Windows)',
 'SubjectDistanceRange': 0,
 'SubjectLocation': (1632, 1224, 3264, 2448),
 'WhiteBalance': 0,
 'XResolution': (240, 1),
 'YResolution': (240, 1)}
```

But there's an additional nested 'GPSInfo' dictionary for some images that we also need to decode the keys for.
Here's how we do that.

```python
from PIL.ExifTags import GPSTAGS as gpstag_num2name

if 'GPSInfo' in exif_data:
    exif_data['GPSInfo'] = dict(
        zip(
            map(lambda i: gpstag_num2name.get(i, i), exif_data['GPSInfo'].keys()),
            exif_data['GPSInfo'].values()
        )
    )
```

That looks like some metadata that might be useful in our database so let's store that in the JSONField we created last week.

## In-Class Exercise

Now it's your turn.
Copy the image_info.py file from this `lessons/14-...` directory into your student work folder.
Add code to it so that it translates the numerical GPSInfo keys into useful string names.
You can do better (more pythonic) than the hacky way we did it above shouldn't be copied.
Then have your script output the entire Exif nested dictionary of metadata to `stdout` using `json.dump()` or `json.dumps()`.
Try not to use the code above.
It's better to be explicit rather than using the super-fast, but hard-to-read, `map` built-in function.
And `lambda`s almost always make your code harder to read and debug.

Test your script on any images you have on your laptop.
Does it display GPSInfo?
Which of your images have GPSInfo and which don't?

Now we can add that script to your django app, so you can import it in a view or model to extract metadata from uploaded images.
Put `image_info.py` in either your `labeler_site` package or your `labeler` django app directory.
Then you can point to it in your setup.cfg so it installs in your $PATH and you can run it from wherever your images are located.

Here's how we did it for `labeler_site/bot.py`.

```ini
[entry_points]
# Add here console scripts like:
# console_scripts =
#     script_name = labeler_site.module:function
console_scripts =
    bot = labeler_site.bot:run
```

Do that for your image_info script.
You may have to create a `run()` function in your script and call it within the `__main__` entry point.
