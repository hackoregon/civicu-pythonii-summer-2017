## Project Scaffolding

I wonder if anyone has built a "best practices" folder structure example for a python project?

```bash
$ pip search "python example project skeleton" | grep skeleton
aimes.skeleton (1.2.0)                              - A Skeleton Generator
ankle (0.4.1)                                       - Find elements in HTML by matching them with a skeleton
ansprogen (0.0.6)                                   - A project generator tools for easy create project skeleton.
django-app-skeleton (1.0.4)                         - A basic skeleton and script to make a packageable django application
django-appskel (1.0a)                               - App for building reusable app skeletons with testsr
bambu-bootstrap (3.3)                               - Use Twitter's Bootstrap CSS framework to build your app. All the views Bambu uses all extend a base 
Bananas (0.1.2)                                     - My Bananas project. Learning how to use project skeletons and make packages.
BlastOff (0.3a2)                                    - A Pylons application template providing a working site skeleton configured with SQLAlchemy, mako, 
python-boilerplate (0.4.10)                         - Creates the skeleton of your Python project.
boilerplate_dcc_pyside_widget (0.0.5)               - Repository for boilerplate PySide DCC widget. This tool serves as barebone,     
```

```bash
$ pip search "python project template" | grep -i templ | grep -i proj
django-templates-admin (0.4.1)                                                       - Edit project template files from the Django admin UI
anvil (0.0.2)                                                                        - Generates new project structures from Jinja templates
templer.django-project-app (1.2)                                                     - Templer extension for creating Django applications within projects.
armstrong.templates.standard (1.0.2)                                                 - Provides a basic project template for an Armstrong project
armstrong.templates.tutorial (1.0.0)                                                 - The tutorial project for Armstrong
ba (0.1.15)                                                                          - CLI utility to interactively create projects from project templates, 
basil_django (0.1)                                                                   - Basil template to create a basic django project.
bids (0.0)                                                                           - bids: a template for small scientific Python projects
bobtemplates.affinitic (1.0)                                                         - Templates for Affinitic Plone projects.
bobtemplates.ecreall (0.6)                                                           - Templates for Ecréall projects.
bobtemplates.fon (0.3)                                                               - Templates for fon projects
bobtemplates.gillux (1.3.0)                                                          - Python project bootstraps for mr.bob: usual Python distro, build
bobtemplates.niteoweb (0.3)                                                          - Templates for NiteoWeb projects.
bobtemplates.odoo (1.1.2)                                                            - mr.bob templates for Odoo projects
bobtemplates.plone (1.0.5)                                                           - Templates for Plone projects.
bobtemplates.sixfeetup (1.0)                                                         - Unified buildout template for Plone projects.
django-cms-boilerplate (1.0)                                                         - Django-cms initial project template
boilerplate (1.2.2-beta)                                                             - Easy to use tool for painless project layout templating
django-html5-mobile-boilerplate (1.0.5)                                              - A framework that includes the Django HTML5 boilerplate template into your django project
django-html5-boilerplate (1.0.8)                                                     - A framework that includes the HTML5 boilerplate template into your django
bootd (1.0.8)                                                                        - Wizard startproject from django base template.
django-bootstrap-email (0.0.1)                                                       - Using Twitter Bootstrap in e-mail templates for Django projects
django-template-bootstrap (0.2.15)                                                   - A django template based on twitter's bootstrap project.
buchner (0.1.dev)                                                                    - Flask project template and helper library 
```

Let's not reinvent the wheel, rather install one called `PyScaffold`

```bash
$ pip install PyScaffold
$ putup --help
$ putup -l mit --with-django --with-travis --with-tox --with-pre-commit civicu_app
```

What have we done?!

```bash
$ cd civicu_app/
(civicu) hobs@spectre:~/src/civicu_app/  master
$ tree
		.
		├── AUTHORS.rst
		├── CHANGES.rst
		├── civicu_app
		│   ├── __init__.py
		│   ├── __pycache__
		│   │   ├── __init__.cpython-35.pyc
		│   │   └── skeleton.cpython-35.pyc
		│   ├── settings.py
		│   ├── skeleton.py
		│   ├── urls.py
		│   └── wsgi.py
		├── civicu_app.egg-info
		│   ├── dependency_links.txt
		│   ├── not-zip-safe
		│   ├── PKG-INFO
		│   ├── requires.txt
		│   ├── SOURCES.txt
		│   └── top_level.txt
		├── docs
		│   ├── authors.rst
		│   ├── changes.rst
		│   ├── conf.py
		│   ├── index.rst
		│   ├── license.rst
		│   ├── Makefile
		│   └── _static
		├── LICENSE.txt
		├── manage.py
		├── README.md
		├── README.rst
		├── requirements.txt
		├── setup.cfg
		├── setup.py
		├── test-requirements.txt
		├── tests
		│   ├── conftest.py
		│   ├── __pycache__
		│   │   ├── conftest.cpython-35-PYTEST.pyc
		│   │   └── test_skeleton.cpython-35-PYTEST.pyc
		│   ├── test_skeleton.py
		│   └── travis_install.sh
		└── tox.ini
```



```bash
$ cd cividu_app
$ tree
```