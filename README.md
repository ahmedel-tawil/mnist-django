# mnist-django
CNN model to classify the hand written digits, with Django 
<img src="/test.png" />

### Prerequistes
1. Django + 4.0
2. Python 3.8
3.tensorflow


### installation 
 clone the project to your directory using the following command 
- git clone https://github.com/ahmedel-tawil/mnist-django.git
 
 inside the projct directory create a python virtual environment using command line with the following command  
 
- virtualenv venv 
- source venv/bin/activate


 install project dependencies. through the following command:
 -pip install -r requirements.txt
 
 
 the project already contains the db.sqlite3 database file so  No Need to  run the migration commands, if you wich to start from the beginning delete the  db.sqlite3, then runs the following inside the project directory 
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser

the next step is to run a develpment to start using the software from th following  command 
- python manage.py runserver
and in our browser navigate to http://127.0.0.1:8000/ 
