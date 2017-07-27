# Class syllabus Python II

## Teachers

* Zak Kent: [zak.kent@gmail.com](mailto:zak.kent@gmail.com)
* Hobson Lane: [hobsonlane@gmail.com](mailto:hobsonlane@gmail.com)
* Mark Wheeler: [wheelerma55@gmail.com](mailto:wheelerma55@gmail.com)

## GitHub: http://github.com/hobson

Welcome to the Civic U Python II class!

We’re super excited that you’re able to take time out of your busy schedule to learn Python with us.
This is a guide to what we will be learning throughout the session.
We will do our best to adhere to this schedule but ask that you be flexible if we need to change the pacing of some lessons based on the speed in which the group can complete them.

## Course description: 

This course will focus on using Python to collect, clean, transform and share data from various 3rd party APIs.
We will also be looking at some features and best practices with Python that fall more towards the intermediate level of the spectrum which you may
not have seen in many introductory tutorials.
Sharing the data we collect will primarily be accomplished using the Django REST Framework (DRF).
The DRF is a super useful tool for building APIs quickly and comes with tons of extra functionality to make our lives easier.
Above all we will be writing code and tests every day that we’re in class and will strive to have a good mix of hands on activities and meaningful
lectures that give real world context to what we’re learning.

## Preparation for class:

When preparing for this class, you should make sure that you have a text editor installed that you’re comfortable with (Sublime Text and Visual Studio Code are both good options).
We will also be using Python 3 so please do your best to have it installed beforehand.
If any of the documentation below gets too tricky feel free to reach out via Slack or wait until the first day of class and we can work on the installation together.

### Installation docs for Python 3: 

* Mac (recommended) : [http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/](https://www.google.com/url?q=http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/&sa=D&ust=1501107467506000&usg=AFQjCNFbbY3DPVB53J3k6LLdMhtGAJRY5w)
* Main installation page (Linux, Mac, Windows): [https://www.python.org/downloads/](https://www.google.com/url?q=https://www.python.org/downloads/&sa=D&ust=1501107467506000&usg=AFQjCNHxsd3uhuvdTXBVzEnOIMje4T-1pw)

If you’re looking for some materials to study before class TreeHouse and Lynda both have good introductory videos.
Also, with a Multnomah county library card you’re able to get a free access to a *Lynda* account :)

[Optional course list](https://www.google.com/url?q=https://docs.google.com/document/d/1kRzzybmQOi_uw2-BWnxZtIEQ5ajo48G4X0WyQ8ByjPE/edit?usp%3Dsharing&sa=D&ust=1501107467507000&usg=AFQjCNEGgBLCbZJkV8e_y5hi5Q7vVHQ9OQ)

### Your Editor and Linter (I like Sublime + Flake8)

Set up your editor to highlight lint in your code when you save!

1. [install sublime](https://www.sublimetext.com/3)
2. [install package control](https://packagecontrol.io/installation)
3. [`shift-ctrl-p` then `install` then `linter` then <enter> or <tab>](http://sublimelinter.readthedocs.io/en/latest/installation.html#installing-via-pc)
4. [`pip install flake8`](https://github.com/SublimeLinter/SublimeLinter-flake8#linter-installation)
5. [`shift-ctrl-p` then `install` then `linter-flake8` then `<enter>` or `<tab>`](https://github.com/SublimeLinter/SublimeLinter-flake8)
6. find the settings for sublime-linter and adjust them to your taste
7. 

Set up your environment to automatically lint your code with every push!

```bash
$ cd ~/src/civicu-pythonii-summer-2017/
$ cp shared-resources/pre-commit .git/hooks/
$ # ln -s shared-resources/pre-commit .git/hooks/pre-commit
$ cp shared-resources/flake8.cfg .git/hooks/
$ # ln -s shared-resources/flake8.cfg .git/hooks/flake8.cfg
$ cp shared-resources/delint_working_dir .git/hooks/
$ # ln -s shared-resources/delint_working_dir .git/hooks/delint_workin_dir
$ git commit -am 'force flake8 linting'
$ git push
```


## Syllabus

Below you’ll find an outline of the topics we’ll be studying in class week by week.
If you have any questions or concerns beforehand feel free to contact me via our Slack channel or by email at [hobsonlane@gmail.com](hobsonlane@gmail.com) I look forward to getting to meet y’all, see you soon!

+--------------------------------------+--------------------------------------+
| ## Date         | ## Class focus  |
+--------------------------------------+--------------------------------------+
| 7/10         | - installation of   |
|                                      | tools                         |
|                                      |                                      |
|                                      | - introduction to   |
|                                      | class structure               |
|                                      |                                      |
|                                      | - git/unix          |
|                                      | basics                        |
|                                      |                                      |
|                                      | - benchmark current |
|                                      | level of Python knowledge     |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge (random group assignment   |
|                                      | tool)                         |
+--------------------------------------+--------------------------------------+
| 7/12         | - review of Python  |
|                                      | basics targeted from benchmark       |
|                                      | survey                        |
|                                      |                                      |
|                                      | - intro into ways   |
|                                      | to debug in Python and general       |
|                                      | problem solving strategies    |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge                     |
+--------------------------------------+--------------------------------------+
| 7/17         | - list              |
|                                      | comprehensions                |
|                                      |                                      |
|                                      | - lazy evaluation & |
|                                      | generators                    |
|                                      |                                      |
|                                      | - using python to   |
|                                      | clean and manipulate csv             |
|                                      | files                         |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge (clean dirty data)  |
+--------------------------------------+--------------------------------------+
| 7/19         | - testing with      |
|                                      | unittest                      |
|                                      |                                      |
|                                      | - tour of Django    |
|                                      |                               |
|                                      |                                      |
|                                      | - manage.py command |
|                                      | basics                        |
|                                      |                                      |
|                                      | - settings &        |
|                                      | installing 3rd party tools    |
|                                      |                                      |
|                                      | - intro to          |
|                                      | manage.py shell\_plus         |
+--------------------------------------+--------------------------------------+
| 7/24         | - testing with      |
|                                      | unittest                      |
|                                      |                                      |
|                                      | - group code        |
|                                      | challenge (unittest)          |
|                                      |                                      |
|                                      | - request/response  |
|                                      | cycle and HTTP                |
|                                      |                                      |
|                                      | - explanation of    |
|                                      | WSGI                          |
+--------------------------------------+--------------------------------------+
| 7/26         | - tour of           |
|                                      | Django                        |
|                                      |                                      |
|                                      | - basic building    |
|                                      | blocks of the DRF             |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge (build a basic             |
|                                      | endpoint)                     |
+--------------------------------------+--------------------------------------+
| 7/31         | - filtering by      |
|                                      | query params                  |
|                                      |                                      |
|                                      | - querysets and     |
|                                      | filtersets                    |
|                                      |                                      |
|                                      | - testing API       |
|                                      | endpoints                     |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge (adding filtering to       |
|                                      | endpoints with tests)         |
+--------------------------------------+--------------------------------------+
| 8/2          | - running scripts   |
|                                      | that have access to django models    |
|                                      | outside of an app             |
|                                      |                                      |
|                                      | - workshop          |
|                                      | (building a script that runs outside |
|                                      | of Django but uses the ORM)   |
|                                      |                                      |
|                                      | - overriding        |
|                                      | inherited methods, uses of           |
|                                      | Super()                       |
+--------------------------------------+--------------------------------------+
| 8/7          | - decorators |
|                                      |                                      |
|                                      | - advanced testing  |
|                                      | with mocks                    |
|                                      |                                      |
|                                      | - using testing     |
|                                      | fixtures                      |
|                                      |                                      |
|                                      | - group challenge   |
|                                      | creating mocks for tests      |
|                                      |                                      |
|                                      |              |
+--------------------------------------+--------------------------------------+
| 8/9          | - connecting to 3rd |
|                                      | party APIs                    |
|                                      |                                      |
|                                      | - introduction to   |
|                                      | scrapy and beautiful soup     |
|                                      |                                      |
|                                      | - gathering data    |
|                                      | and adding it to Django       |
|                                      |                                      |
|                                      | - group challenge   |
|                                      | (gather data and write it to         |
|                                      | csv)                          |
+--------------------------------------+--------------------------------------+
| 8/14         | - 3rd party APIs    |
|                                      | continued                     |
|                                      |                                      |
|                                      | - transformation of |
|                                      | gathered data                 |
|                                      |                                      |
|                                      | - load the csv of   |
|                                      | gathered data to Django       |
|                                      |                                      |
|                                      | - expose the loaded |
|                                      | data through custom endpoints |
+--------------------------------------+--------------------------------------+
| 8/16         | - functional        |
|                                      | programming                   |
|                                      |                                      |
|                                      | - bottom up         |
|                                      | approach to problem solving   |
|                                      |                                      |
|                                      | - modeling          |
|                                      | solutions on simple data             |
|                                      | representation of problem     |
|                                      |                                      |
|                                      | - work on student   |
|                                      | APIs                          |
+--------------------------------------+--------------------------------------+
| 8/21         | - functional        |
|                                      | programming continued         |
|                                      |                                      |
|                                      | - mini group        |
|                                      | project using functional stuff we’ve |
|                                      | learned                       |
|                                      |                                      |
|                                      | - work on student   |
|                                      | APIs                          |
+--------------------------------------+--------------------------------------+
| 8/23         | - deploying APIs    |
|                                      |  (heroku)                     |
|                                      |                                      |
|                                      | - brief explanation |
|                                      | of additional deployment             |
|                                      | options                       |
|                                      |                                      |
|                                      | - working on        |
|                                      | student projects              |
+--------------------------------------+--------------------------------------+
| 8/28         | - GraphQL and how   |
|                                      | it can be added seamlessly to an     |
|                                      | existing project              |
|                                      |                                      |
|                                      | - paired code       |
|                                      | challenge (using GraphQL)     |
|                                      |                                      |
|                                      | - start building a  |
|                                      | GraphQL server for our               |
|                                      | projects                      |
+--------------------------------------+--------------------------------------+
| 8/30         | - GraphQL continued |
|                                      |                               |
|                                      |                                      |
|                                      | - sharing student   |
|                                      | projects                      |
|                                      |                                      |
|                                      | - open ended        |
|                                      | session on topics that needed more   |
|                                      | time                          |
+--------------------------------------+--------------------------------------+
