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

```
import PIL.Image
img = PIL.Image.open('../shared-resources/')
exif_data = img._getexif()