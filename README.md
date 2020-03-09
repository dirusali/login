# this is django project called login and a django app called home
# it allows administrators to log in using their google account

**Setup**

$ sudo -H pip3 install virtualenv

$ mkdir ~/login
$ cd ~/login
$ virtualenv myenv
$ source myenv/bin/activate

$ django-admin.py startproject login ~/login
$ python manage.py startapp home
Update your settings to onnect your database:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

$ python manage.py makemigrations
$ python manage.py migrate # to apply migrations
$ python manage.py createsuperuser # to create an administrator user for yourself
$ python manage.py runserver # to run the server

# Now you can go to your localhost/admin and login. You will see google registered in social accounts and you can go to users and create new ones.

# Docker compose testing

You can clone the project in another directory for testing environment and use the Dockerfile and  docker-compose .yml file provided here to run your test.

First update your database settings to:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

and give ownership to your user for the folders with the app:

$ sudo chown -R user:user

use the following command to create the project:

$ docker-compose run web django-admin.py startproject composeexample .

Then to launch the app in your local server run:

$ docker-compose up -e POSTGRES_PASSWORD=YOUR_PASSWORD
Then you can run commands like so:

To run django commands in the test environments with docker-compose you can run:

$ docker-compose run web ... # place here your command for example manage.py migrate


