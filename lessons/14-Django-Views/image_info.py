import os
import django
from django.conf import settings  # Django magic starts here

# `labeler_site` must be a python package installed in your environment (virtualenv)
# OR "install" it manually before running this: `export PYTHONPATH=$PYTHONPATH:/path/to/labeler_site_basedir/`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labeler_site.settings')
django.setup()