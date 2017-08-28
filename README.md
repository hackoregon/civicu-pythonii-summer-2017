# Python II (Advanced Python) Hack University Course

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

