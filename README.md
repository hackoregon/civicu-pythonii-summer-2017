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

### Here's the Original Syllabus

```
    Date     | Topics                                                                    | Challenge  
    -------------------------------------------------------------------------------------------------  
01  Mon 7/10 | class structure, tools: bash, git, pair coding                            | exercism hello world  
    Wed 7/12 | Python review, debugging, problem solving strategies                      | exercism for loop  
02  Mon 7/17 | list comprehentions, generators and lazy evaluation, cleaning csv files   | read & write csv  
03  Wed 7/19 | Django, `manage.py`, `settings.INTALLED_APPS`, `shell\_plus`              | `runserver` with hello world  
04  Mon 7/24 | WSGI, `unittest`, HTTP request/response cycle                             | sum PDX homeless count requests  
    Wed 7/26 | Django Rest Framework (DRF)                                               | build an endpoint  
05  Mon 7/31 | Django `Model.objects.filter`, `querysets`, testing API endpoints         | filter your endpoint, test  
06  Wed 8/02 | use ORM (models.py) outside of django manage.py, `Super()`                | bot that modifes database  
07  Mon 8/07 | fixtures, mocks, and decorators for testing                               | create a fixture to test a django app  
08    Wed 8/09 | scraping (Beautiful Soup) and 3rd party APIs                              | download some tweets from twitter   
09  Mon 8/14 | Data Wrangling with Pandas                                                | Pandas and Exercism
    Mon 8/14 | Scrapy bots to gather data                                                | Scrapy challenge    
    Wed 8/16 | functional programming, bottom's up approach to problem solving           | improve student API  
    Mon 8/21 | advanced functional programming                                           | improve student API  
    Wed 8/23 | deployment (heroku)                                                       | deploy your django app  
    Mon 8/28 | GraphQL                                                                   | Graph Query challenge  
    Wed 8/30 | More GraphQL                                                              | Graph Query challenge  
```

### Updated Syllabus

```
Date     | #  |Topics                                                                | Challenge
-------------------------------------------------------------------------------------------------
Mon 7/10 | 00 | class structure, tools: bash, git, pair coding                       | exercism hello world
Wed 7/12 | 00 | Python review, debugging, problem solving strategies                 | exercism for loop
Mon 7/17 | 01 | Python3, Showoff, Exercism, git, slack                               | exercism challenge
Wed 7/19 | --                                                                        |
Mon 7/24 | 03 | API clients using `requests` and URL hacking                         | sum PDX homeless counts
Wed 7/26 | 04 | A django project: virtualenv, docs, tests                            | `putup` a django app and create a virtualenv
Mon 7/31 | 05 | document, test, then code                                            | bot.py to respond to user greeting
Wed 8/02 | 06 | Your first django app: image labeling game                           | enable user upload of an image
Mon 8/07 | 07 | Django admin and Django Rest Framework (DRF)                         | build an endpoint
Wed 8/09 | 08 | Django `Model.objects.filter`, `querysets`, postgresql               | filter your endpoint, test 
Mon 8/14 | 09 | Using Pandas for data wrangling, PIL for image manipulation          | plot histogram of an image's pixels (spectrogram)
Wed 8/16 | 10 | Dynamic programming (graph search)                                   | algorithm for least change problem
Mon 8/21 | 11 | GraphQL
Tue 8/22 | 12 | Makeup class
Wed 8/23 | 13 | Functional programming
Mon 8/28 | 14 | Continuous integration: Travis, Coveralls, CodeHealth, Insping
Tue 8/29 | 15 | Makeup class
Wed 8/30 | 16 | Final Exam
```
