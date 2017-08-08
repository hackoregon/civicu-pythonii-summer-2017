## Resources:





#### 1. Clone repo
- Make a directory and clone this repo inside
- cd into the ```Hack_O_DjangoREST_Tut``` repo

#### 2. Make a virtual environment 
Complete these steps inside the ```Hack_O_DjangoREST_Tut``` repo 
- Setup a virtual environment: 
  - Depending on where your version of Python 3 is installed you may need to alter the path in the command below
  - ```virtualenv -p /usr/local/bin/python3 venv3``` 
- Activate virtual environment: 
  - ```source venv3/bin/activate``` 
  - command above activates the virtual environment your command line prompt should start with ```(venv3)``` if it worked
  
#### 3. Install depencencies with pip
In the top level of the cloned repo there is a ```requirements.txt``` file  
- Install depedencies from requirements.txt: 
  - pip install -r requirements.txt  
  
#### 4. Start server
- cd into the ```example_project``` directory. Should contain the ```manage.py``` file.
- In directory with ```manage.py``` run this command: 
  - ```python manage.py runserver``` 
  - see working endpoint at: [http://localhost:8000/songs/](http://localhost:8000/songs/)
    
## Example file structure of a starter project
Below is what the file structure looked like after running a basic setup found here: [new_project_setup](http://www.django-rest-framework.org/tutorial/quickstart/) 
![tree structure of project](./images_readme/file_structure.png?raw=true "Optional Title")

## Basic building blocks of endpoints 
![tree structure of project](./images_readme/DRFpieces.png?raw=true "Optional Title")

The image above outlines the pieces that need to be in place for an endpoint to work in the DRF assuming that the basic setup of the project has already been done.








  
