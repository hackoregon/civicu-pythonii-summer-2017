import os
import sys
import json

import django
from django.conf import settings  # noqa Django magic starts here

import PIL.Image
from PIL.ExifTags import TAGS as tag_num2name


# `labeler_site` must be a python package installed in your environment (virtualenv)
# OR "install" it manually before running this: `export PYTHONPATH=$PYTHONPATH:/path/to/labeler_site_basedir/`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labeler_site.settings')
django.setup()


if __name__ == '__main__':
    if len(sys.args) > 1:
        image_path = ' '.join(sys.args[1:])
    else:
        os.path.join(settings.BASE_DIR, 'labeler', 'data', 'SUNP0254.jpg')
    img = PIL.Image.open(image_path)
    exif_data = img._getexif()
    # pprint(exif_data)
    # {271: 'Icatch',
    #  272: 'WF121',
    #  282: (240, 1),
    #  283: (240, 1),
    #  296: 2,
    #  305: 'Adobe Photoshop Lightroom 4.4 (Windows)',
    #  306: '2016:07:31 14:16:14',
    #  33434: (1, 60),
    #  33437: (32, 10),
    #  34665: 200,
    #  34850: 2,
    #  34855: 100,
    #  36864: b'0230',
    #  36867: '2014:04:27 17:40:29',
    #  36868: '2014:04:27 17:40:29',
    #  37377: (5906891, 1000000),
    #  37378: (3356144, 1000000),
    #  37379: (-5000, 1000),
    #  37380: (0, 10),
    #  37381: (3, 2),
    #  37383: 4,
    #  37384: 0,
    #  37385: 1,
    #  37386: (82, 11),
    #  37396: (1536, 1152, 3072, 2304),
    #  41728: b'\x03',
    #  41729: b'\x01',
    #  41985: 0,
    #  41986: 0,
    #  41987: 0,
    #  41988: (0, 1),
    #  41990: 0,
    #  41991: 0,
    #  41992: 0,
    #  41993: 0,
    #  41994: 0,
    #  41996: 0}

    exif_data = dict(
        zip(
            map(tag_num2name.get, exif_data.keys()),
            exif_data.values()
        )
    )
    print(json.dumps(exif_data, indent=2))
