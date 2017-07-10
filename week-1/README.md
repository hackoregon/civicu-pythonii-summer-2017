# Python level II Day 1 

## Welcome!!!
Thank you all for being willing to take time out of your day to learn some Python! It's our goal in this class to provide students with the skills needed to start making real projects and to be able to access and collect data. We will be focusing primarily on the backend side of things and will spend most of our time working with 3rd party APIs as well as building our own using the Django REST Framework. Day one of this class will focus on setting things up so that we'll be successful throughout the rest of our time together. Below you'll find a list of class objectives and information about the tools we'll be using during the next 8 weeks. 

### Tonight's objectives
* Get to know one another
* Introduce the `showoff` tool
* Review syllabus - Google Classroom
* Class communication channels (Slack, email, GitHub)
* Get working dev environment setup (Python 3, setting up virtualenvs)
* Explain how we will use Git and GitHub (forking repos, setting upstream repo, pushing to fork)
* Introduce Exercism tool and solve a paired code challenge
* Take Python general knowledge survey

## Class communication channels
* [Link to Class Slack Channel](https://hackusummer2017.slack.com)
* Email zak.kent@gmail.com

## Introduction to the `showoff` presentation tool
We will be using a presentation tool called `showoff` in class that runs a web app and allows students to interact with presentations as they happen. In order to interact with a presentation you'll need to go to the URL and port provided by the instructor in your web browser. The URL will change every class so it will be provided daily in the Slack channel.  

##### Notable features we'll be using:
* Interactive anonymous quizes
* Ability to ask anonymous questions during a presentation

## Setting up your environment

#### Python 3 install
* [Python 3 install on Mac with Brew](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
* [Main installation page](https://www.python.org/downloads/)

#### Possible text editors
* [Sublime Text 3](https://www.sublimetext.com/3)
* [Visual Studio Code](https://code.visualstudio.com/)

#### Virtual environments
* [Article on virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

## Using Git & GitHub
Throughout this course we will be using Git and GitHub as a convenient way to share code with one another and to monitor student's progress. Bellow you'll find a link to an interactive GitHub tutorial and instructions for how we will share work with one another. 

* [Link to interactive GitHub tutorial](https://try.github.io/levels/1/challenges/1)

#### Steps for class GitHub setup
* Fork the class repo to your GitHub account
  * [class repo](https://github.com/Zak-Kent/Hack_O_class)
* Clone the forked repo onto your local machine
  * `git clone <github_url_to_forked_repo>`
* Run the command `git remote -v` you should see your the repo your forked to your GitHub as `origin`
* Link your forked repo to the original
  * [docs on configuring a remote fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
* Sync your forked repo with the original
  * We will follow the process in the link below to get new code for each day in class
  * [docs on syncing a fork](https://help.github.com/articles/syncing-a-fork/)
* Make a new directory using your name as the title inside the `student-work` directory in the class repo
* Inside your newly created directory use the command `touch README.md` to create a new README.md file 
* Use git to add and commit the file you just created
* Push the changes to your GitHub fork (called `origin`) with the command `git push origin master`
* Go to GitHub and make a pull request against the class repo with your changes

## Introduction to Exercism
[Exercism.io](http://exercism.io/languages/python/about) is a really cool learning resource that has a selection of ready made code challenges with included tests that we will use occasionally during our course. We will only use the code challenges in Exercism when they apply directly to what we're learning but will follow a similar format for custom in class challenges.

In order to get Exercism setup on your computer please follow the link below: 
[Exercism CLI install](http://exercism.io/clients/cli)

Once the CLI for Exercism is installed run the command `exercism fetch python word-count` to get the mini exercise we will be solving as a group. Once you've solved the problem push the solution with `exercism submit <path_to_solution_file>`. While you're solving this problem you should receive an invite to the Exercism team for our class. This will allow students to comment on each others solutions and share the different problems they've solved. 

## Python general knowledge survey
The link below will lead you to a survey about your current level of Python knowledge. It's completely anonymous and will be used as a way to tailor instruction according to the needs of the class. We ask that you complete the form before leaving tonight and do so without looking up answers while you're filling it out. It's perfectly ok if you aren't familiar with everything in the survey, just fill out what you can.
[Python Knowledge survey](https://docs.google.com/forms/d/1cqpVhViQ9-lPPHKQfqSUxEW19RoQCBIoi7SOaR6PmWo/viewform?edit_requested=true)
