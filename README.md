# login
this is django app that allows administrators to log in using their google account
**Setup**
$ sudo -H pip3 install virtualenv

$ mkdir ~/login
$ cd ~/login
$ virtualenv myenv
$ source myenv/bin/activate

(myenv) $ django-admin.py startproject login ~/login



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
