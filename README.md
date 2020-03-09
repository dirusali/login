# this is django project called login and a django app called home, it allows administrators to log in using their google account

**Setup**
```
First install pip and create your environment:

$ sudo -H pip3 install virtualenv

$ mkdir ~/login

$ cd ~/login

$ virtualenv myenv
```

Activate your environment, install requirements and start a django project:

```
$ source myenv/bin/activate
$ pip install -r requirements.txt
$ django-admin.py startproject login ~/login
$ python manage.py startapp home
```

Update your settings apps and connect your database:

```
INSTALLED_APPS = [
 ‘django.contrib.admin’,
 ‘django.contrib.auth’,
 ‘django.contrib.contenttypes’,
 ‘django.contrib.sessions’,
 ‘django.contrib.messages’,
 ‘django.contrib.staticfiles’,
 ‘django.contrib.sites’,   # <--
 ‘social_app’,   # <--
 
 ‘allauth’,   # <--
 ‘allauth.account’,   # <--
 ‘allauth.socialaccount’,   # <--
 ‘allauth.socialaccount.providers.google’,   # <--
]

AUTHENTICATION_BACKENDS = (
 ‘django.contrib.auth.backends.ModelBackend’,
 ‘allauth.account.auth_backends.AuthenticationBackend’,
 )
 
SITE_ID = 1
LOGIN_REDIRECT_URL = ‘/’

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}





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
```

Now you can go to your localhost/admin and login. You will see google registered in social accounts and you can go to users and create new ones.


# Docker compose testing


You can clone the project in another directory for testing environment and use the Dockerfile and  docker-compose .yml file provided here to run your test.


First update your database settings to:


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

```
and give ownership to your user for the folders with the app:

```
$ sudo chown -R user:user
```

use the following command to create the project:

```
$ docker-compose run web django-admin.py startproject login .
```

Then to launch the app in your local server run:

```
$ docker-compose up -e POSTGRES_PASSWORD=YOUR_PASSWORD
```

To run django commands in the test environments with docker-compose you can run:

```
$ docker-compose run web ... # place here your command for example manage.py migrate
```


