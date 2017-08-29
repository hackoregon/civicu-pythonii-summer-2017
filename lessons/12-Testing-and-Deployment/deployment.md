# Deployment

1. provision: get a server set up with your requirements.txt and a webserver
2. configure: get the web server and other daemon's configured to serve your app
3. upload: push your code to the server
4. launch: run the webserver and your app
5. plumbing: expose the URL/IP to the public so they can issue requests to it

## Five Ways to Deploy a Webapp

1. ngrok: Expose your runserver on your laptop. Great for customer demo!
2. Heroku: Any gunicorn wsgi app (like Django) is supported "out of the box".
3. AWS Lambda: serverless (Lambda spins up only when someone requests your site)
4. VM on Google Web Services (or AWS EC2). Uses ssh to get your app pushed.
5. Docker

[YouTube Demo by Andrew Baker](https://youtu.be/vGphzPLemZE)

[Heroku, Ngrok, Docker, and Lambda config files](https://github.com/atbaker/five-ways-to-deploy)

### Ngrok

Download the version you need:

[download ngrok binary](https://ngrok.com/download)

#### Install Ngrok in your PATH

If you only want to use ngrok once, you can just put it in the same directory as your `manage.py` file.
But if you want to be able to use it again anytime your boss says "what have you been up to lately?" then you'll want to put it system PATH so you can run it whenver/wherever you like.

If you want to use the python console to do this launch python and then use your `getenv` and `os` skills to do something like this:

```python
import os
pathsep = os.pathsep  # in case your system PATH separator is not ":"
# find the first path listed in your PATH variable
first_path = os.path.abspath(os.getenv('PATH').split(pathsep)[0])

os.rename('ngrok', os.path.join(first_path, 'ngrok'))
```

If you like your OS shell (usually `bash`) more than `python`, and want to use it to manipulate your path and move files around then here's another way to do it. You can put ngrok in a new ~/src/bin directory and then add that directory to your system `PATH` like this:

```bash
mkdir -p ~/src/bin
mv ngrok ~/src/bin
export PATH="$PATH:$HOME/src/bin/"
```

And you can append this last line to your `.bashrc` or `.profile` to modify your `PATH` every time you start a shell like this:

```bash
echo 'PATH="$PATH:$HOME/src/bin/"' >> ~/.bashrc
```

Add ngrok.io to your ALLOWED_HOSTS in settings.py

```python
ALLOWED_HOSTS = ['localhost', '.ngrok.io', '.totalgood.org', '.totalgood.com']
```

Runserver and run ngrok:

```bash
python manage.py runserver
```

Check that it's running on [localhost:8000](http://localhost:8000)

Tell ngrok which port to expose and what port it should look like to the public.
The `http` commandline arg below is shorthand for `80`:

```bash
ngrok http 8000
```

"Grep" for the `*.ngrok.io` public URL where your app is receiving requests from and browse to it to check it out!

Browse to it from your phone before you send it to your boss to make sure it's working. 

```bash
firefox http://6af05f51.ngrok.io
```

And, even cooler, you can [watch the raw GET requests roll in](http://localhost:4040/inspect/http)!

### Heroku

[Heroku Tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

```bash
sudo apt install python3.6
mkvirtualenv -p python3.6 herokuenv
echo '/home/hobs/src/labeler_site/' > ~/.virtualenvs/herokuenv/.project
workon # source ~/.virtualenvs/herokuenv/activate
pip install gunicorn
```

Install the heroku toolbelt (command line tool), but before you copy-paste this, you need to type a command like this to log into sudo and provide your password: `sudo echo hi`. 

```bash
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
``` 

Get into your django app BASE_DIR and then tell heroku that this is an app you want to associate with your account.

```bash
heroku create
```

This will ask for your heroku credentials so you can log in.
Then you can push to the `git remote` it created for your app to upload your code:

```bash
git push heroku master
```


## In-Class Excercise

Deploy your app using one of the methods above (preferably both).
I can help with any of them, but I'm most experienced with ngrok, AWS EC2, and heroku.


