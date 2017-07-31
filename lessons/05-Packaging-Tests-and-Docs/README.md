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

#### setup.py and setup.cfg

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

#### Releasing a Package

```
$ git tag -a 0.0.1 -m 'Release of version 0.0.1 does awesome new stuff!'
$ git push --tag
$ python setup.py build sdist bdist --universal
$ pip install twine
$ twine upload build/*.tgz
```


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



# Quiz