# sicario
SICARIO

## Create the database and apply the permissions
```
$ mysql
$ CREATE DATABASE sicario CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
$ CREATE USER 'sicario'@'localhost' IDENTIFIED BY 'password';
$ GRANT ALL PRIVILEGES ON *.sicario TO 'sicario'@'localhost';
```

## Install Python 3
$ apt install python3

## Install Pip 3
$ apt install python3-pip

## Install Django Project
$ python3 -m pip install Django

## Generate Secret Key
$ python3 -c 'from django.core.management.utils import get_random_secret_key; print (get_random_secret_key())'

## Create .env
```
DEBUG=True
SECRET_KEY=
DB_ENGINE=django.db.backends.mysql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

## Install Decouple
$ pip3 install python-decouple

## Install Crispy Forms
$ pip3 install --user django-crispy-forms

## Install
$ pip3 install django-widget-tweaks

## Install Mysql Python Client
$ sudo apt install python-dev default-libmysqlclient-dev

## Install Mysql Client on Django
$ pip3 install mysqlclient

## Run Migrates
$ python3 manage.py makemigrations
$ python3 manage.py migrate

## Create Superuser
$ python3 manage.py createsuperuser

## Run Collectstatic
$ python3 manage.py collectstatic

## Install Filetype
$ pip3 install filetype

## Install Clean Up
$ pip3 install django-cleanup

## Run Project
$ python3 manage.py runserver

## Install Snap
$ sudo apt install snap

## If necessary

### Install Bower
$ sudo snap install bower --classic

### Update AdminLte
$ cd static

$ bower install admin-lte

