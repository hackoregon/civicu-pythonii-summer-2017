# Today

1. Attendance and Quiz (20 min)
2. Show and Tell (Code Review) (20 min)
3. Workshop
  3a. Packaging (30 min)
  3b. Docs (20 min)
  3c. Tests (1 hr)
4. Challenge (10 min)

## Review

- What does an HTTP GET request URL look like?
- What is PyScaffold?
- Are there alternatives?
- What does `putup` do
- Name one `putup` option and what it does
- Name one folder or file that `putup` creates
- Name files that `putup --with-django` creates
- `django-admin startapp`? [RTD](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
- `django-admin startproject`?
- What is the e-mail address associated with your git commits?
- What is the e-mail address associated with your githib profile?
- What is the name associated with your git commits?
- What is the name associated with your github profile?
- How can you change these?
- How can you change git settings in your local repo?
- How can you change git settings for all your git repos (past and future)?
- How can you change your github settings for all your github repos?
- What is the Socratic method

Let's make sure you have a virtualenv you can use for your app and you can switch to it easily to start work whenever inspiration hits.

```bash
mk virtualenv civicu_app
nano ~/.virtualenvs/civicu_app/.project
workon civicu_app
pip install Pillow
```

## Packaging, Docs, and Tests

### Python Packages

- What is a python module?
- What is a python package?
- Where does `import` look for packages and modules?
- What is the difference between a relative and absolut import?
- Can I import from the current working directory in ipython?
- How do I upload my file to pypi?
- Challenges/problems with pypi
- Can I host my own pypi?
- Can I mirror pypi?
- What is `setup.py`?
- What is `setup.cfg`?
- What is an egg?
- What goes in the .egg-... directory?
- Can I delete it?
- What is a wheel?
- What goes in the `build/` dir?
- Can I delete it?


#### [setup.py](https://packaging.python.org/tutorials/distributing-packages/#setup-args)

```bash
$ python setup.py --help
Common commands: (see '--help-commands' for more)

  setup.py build      will build the package underneath 'build/'
  setup.py install    will install the package

Global options:
  --verbose (-v)      run verbosely (default)
  --quiet (-q)        run quietly (turns verbosity off)
  --dry-run (-n)      don't actually do anything
  --help (-h)         show detailed help message
  --no-user-cfg       ignore pydistutils.cfg in your home directory
  --command-packages  list of packages that provide distutils commands

Information display options (just display information, ignore any commands)
  --help-commands     list all available commands
  --name              print package name
  --version (-V)      print package version
  --fullname          print <package name>-<version>
  --author            print the author's name
  --author-email      print the author's email address
  --maintainer        print the maintainer's name
  --maintainer-email  print the maintainer's email address
  --contact           print the maintainer's name if known, else the author's
  --contact-email     print the maintainer's email address if known, else the
                      author's
  --url               print the URL for this package
  --license           print the license of the package
  --licence           alias for --license
  --description       print the package description
  --long-description  print the long package description
  --platforms         print the list of platforms
  --classifiers       print the list of classifiers
  --keywords          print the list of keywords
  --provides          print the list of packages/modules provided
  --requires          print the list of packages/modules required
  --obsoletes         print the list of packages/modules made obsolete

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help
```

```bash
$ python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  check             perform some checks on the package
  upload            upload binary package to PyPI

Extra commands:
  rotate            delete older distributions, keeping N newest files
  install_egg_info  Install an .egg-info directory for the package
  easy_install      Find/get/install Python packages
  develop           install package in 'development mode'
  rpm_version       Output the rpm *compatible* version string of this package
  bdist_egg         create an "egg" distribution
  saveopts          save supplied options to setup.cfg or other config file
  setopt            set an option in setup.cfg or another config file
  bdist_wheel       create a wheel distribution
  alias             define a shortcut to invoke one or more commands
  upload_docs       Upload documentation to PyPI
  egg_info          create a distribution's .egg-info directory
  doctest           (no description available)
  test              run unit tests after in-place build

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help
```

#### [`setup.cfg`](https://packaging.python.org/tutorials/distributing-packages/#setup-cfg)

*.cfg files are also called INI files. INI files are those configuration/settings files that contain sections and a list of setting values. The INI format is a [`declarative`](https://en.wikipedia.org/wiki/Declarative_programming) Domain-Specific Language (DSL). Python is an [_imparative_ or _procedural_ language](https://en.wikipedia.org/wiki/Imperative_programming).

- What is a DSL?
- What is a "declarative" language?
- What is a "procedural" or "imperative" language?


DSLs are special-purpose languages that are designed and undertstood by all experts in a domain (like Automotive Manufacture, Database Design, Software Design, etc) for a specific, constrained environment, like document or image rendering, or database schema and query definition.

##### Example DSLs:

- markup languages: markdown, HTML, XML, JSON?, CSV?, *.CFG, *.INI, natural language grammar diagramming/tagging (SyntaxNet)
- model and data-specification languages: Ansible yml files, Puppet language, Makefile, *.dot, regex, Swagger API schema definition, `man` and `--help` grammar syntax

DB schema languages, like SQL, CASE, and even UML (universal modeling language), are too general-purpose to be considered domain-specific (I think).

##### Example Declarative Languages

- Puppet Lang (ruby+)
- Ansible *.yml files
- INI/config files
- SQL (sort-of)
- JSON (sort-of)

##### Example Procedural and OO Languages

- Python
- Ruby
- C++

##### Working with INI files (like `setup.cfg`) in python

To load a *.cfg or *.ini file, we use the configparser package built into Python.

```python
import configparser

config = configparser.ConfigParser()
config.read('FILE.INI')
print(config['DEFAULT']['path'])
```

Unlike json, I haven't found a way to convert a config object into a `list` or `dict` except by usinge the `__dict__` attribute.

To update a 'path' configuration parameter in the _DEFAULT_ section of your `config` you would do something like...

```python
config['DEFAULT']['path'] = '/var/shared/'
config['DEFAULT']['default_message'] = 'Hey! help me!!'   # creat…
```


#### [Releasing a Package](https://packaging.python.org/tutorials/distributing-packages/)



We won't do this until after we have some documentation and code, but here's how you can share your awesome new app with the python world.

```bash
$ git tag -a 0.0.1 -m 'Release of version 0.0.1 does awesome new stuff!'
$ git push --tag
$ python setup.py sdist bdist_wheel --universal upload  # INSECURE!!!
```

But that would send a GET and POST requests to *http://*pypi.python.org rather than *https://*! So your packets could be intercepted by the router, or if you're on an unencrypted WiFi connection, anyone on the same WIFI connection!  I'm not sure how hard it is to intercept and decrypt your packets on a password-protected encrypted WiFi network (e.g. WPA2 connection), but better safe than sorry, *especially* if you use the same password at _pypi_ as elsewhere.

```bash
$ pip install twine
$ python setup.py sdist bdist_wheel --universal
$ twine upload build/*.tgz
```

[Twine](https://pypi.python.org/pypi/twine) uses SSL for the connection and is configurable with environment variables in addition to a pypirc file. 

To avoid having to enter your pypi credentials every time you interact with pypi, save something like this to the `~/.pypirc` file:

```ini
[distutils]
index-servers =
    pypi

[pypi]
repository: https://www.python.org/pypi
username: $PYPI_USER
password: $PYPI_PASSWORD
```

Delete the `repository` assignment. It's deprecated in python3 and Twine.

#### Installing

A python package can be installed from a source code path, or .tar.gz or .tgz (tar and gzip bundle) file (which is a wheel). And it can automatically find that wheel if it's registered with pypi and uploaded.

```bash
$ pip install -e path/to/your/python_package/

$ sudo pip install -e path/to/your/python_package/

$ pip install python_package

$ cd python_package
$ python setup.py install

$ cd python_package
$ python setup.py build
$ python 

```

_PyScaffold_ makes it easy to create and install a command line app (like grep or ls or django-admin) with a python package.
Look in `setup.cfg` for a skeleton command line app and the example `skeleton.py` file.

### Docs

- What are docstrings?
	- What do RST docstrings look like?
	- What do Google-style docstrings look like? [RTD](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
	- Which do you prefer?
- Can docstrings produce docs?
- What is Sphinx?
- What is docs/config.py?

Another convention that I find useful is to always use single quotes for 'string's that are intended for a machine and would break your code if they didn't precisely match what the code expects. "Double quotes" are used for all other strings, typically natural language names and phrases that have a lot of different forms that would work in your code.

### Tests

- What is Test-Driven Development (TDD)?
- What is Conference-Driven Development (CDD)?
- What is D&D?
- What is a Unittest?
- What is an Integration Test or E2E (EndToEnd) Test?
- What is Travis?
- What is Tox?
- What is Continuous Integration?
- How do you run tests on a python app?
- How do you run tests on a Django app?
- How can you test web pages?
- How can you test APIs?
- What database or "environment" do your tests use?

Integration testing is hard, and requires a complete E2E app to be useful. But some people argue that they are the only tests you need. I find that unittests are very valuable for functions and classes that are the foundation for something bigger. They are especially important if the wrong output will not trigger an obvious error down the road.

That brings us to a best-practice for Exceptions in web applications. Web applications should minimize the use of `try:`...`except:` blocks, especially "bare" except blocks that will vacuum up *ALL* errors in your code. This is because we want to discover bugs during testing and fix them before they cause unexpected or erroneous behavior for users. Exceptions will log themselves to a log file in a web application rather than hiding themselve and present some default value to the user.  Imagine if, when making a withdrawal from an online ATM or a transfer at a banking web app and you attempted to use a value that wasn't valid (like Euros at a US bank). If that exception were "caught" and a default withdrawal of $0.00 was issued to your account and provided to you, you would be confused. Even more confusing if it assumed that you wanted it to convert those Euros to dollars and withdrew that new, larger amount.


# Quiz

- What is a DSL?
- Where do we configure a command line app in a setup.cfg?
- When does a command line app get inserted into your path?
- Where does it go (what is its path)?
-
