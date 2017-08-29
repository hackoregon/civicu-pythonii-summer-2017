# Syllabus

Below you’ll find an outline of the topics we’ll be studying in class week by week.
If you have any questions or concerns beforehand feel free to contact me via our Slack channel or by email at [hobsonlane@gmail.com](hobsonlane@gmail.com) I look forward to getting to meet y’all, see you soon!

## Course Material Directory Structure

```text
├── 00-Overview
│   └── course-requirements.md
├── 01-Intro-Python3-Showoff-Exercism-Git-Slack
│   ├── git.md
│   ├── README.md
│   └── word_count.py
├── 02-CSV-files
│   ├── CSV_files.md
│   └── README.md
├── 03-HTTP-and-APIs
│   ├── CHALLENGE--Count_Homeless_PDX
│   ├── homeless.csv
│   ├── HTTP_requests.md
│   ├── one-solution-pdx-homeless.md
│   ├── pandas-shortcut.md
│   ├── quiz-help-and-requests.md
│   └── README.md
├── 04-Environments-and-Folder-Structure
│   ├── CHALLENGE--virtualenv-and-conda.md
│   └── project_scaffolding.md
├── 05-Packaging-Tests-and-Docs
│   ├── CHALLENGE--command-line-script.md
│   ├── playground.md
│   └── README.md
├── 06-Django-MTV
│   ├── CHALLENGE-upload-image-to-django-app.md
│   └── README.md
├── 07-Django-Admin-and-APIs
│   ├── CHALLENGE--Labeler-API-Client.md
│   └── README.md
├── 08-Django-with-existing-Database
│   ├── CHALLENGE--database-normalization.md
│   └── README.md
├── 09-Pandas
│   ├── data-wrangling-with-Pandas.md
│   ├── README.md
│   ├── Untitled.md
│   └── upload-file-with-POST.md
├── 10-Advanced-Python
│   ├── advanced-python.md
│   ├── dict-zip-star.md
│   ├── files-and-paths.md
│   ├── python-scripts.md
│   └── README.md
├── 11-Classes-and-Django
│   ├── CHALLENGE.md
│   ├── classes.md
│   ├── django.md
│   ├── exercisms.md
│   └── README.md
├── 12-Testing-and-Deployment
│   ├── deployment.md
│   ├── excercisms-7-8.md
│   ├── image-transformation.md
│   ├── README.md
│   └── testing.md
├── 13-Django-ORM
│   ├── django-orm.md
│   └── README.md
├── 14-Django-Views
│   ├── README.md
│   └── testing-views.md
├── 15-Exam
│   └── README.md
```

Some exercism solutions can be found in `student-work/hobson_lane/exercism/python/`. Exercism help is also available through the exercism.io forum and website.

Any coding challenges you submit must be placed in a folder with your name within the student-work folder.

## Original Schedule

```text
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

## Updated Schedule (WIP)

```text
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
