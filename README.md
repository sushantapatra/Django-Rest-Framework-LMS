## DJANGO REST FRAMEWORK LMS PROJECT 

### BASIC REQUIREMENTS

# `pip install virtualenv`
# `virtualenv venv`
# `venv\Scripts\Activate`

## START PROJECTS

# `pip install django`
# `pip install djangorestframework==3.14.0`
# `pip install markdown`       # Markdown support for the browsable API.
# `pip install django-filter`  # Filtering support
# `pip install mysqlclient`


# `django-admin startproject LMS`
# `cd LMS`
# `python manage.py runserver`

# `python manage.py startapp course`
# `python manage.py startapp chapter`
# `python manage.py startapp order`
# `python manage.py startapp coupon`
# `python manage.py startapp review`
# `python manage.py startapp doubt`

### register the app inside setting.py



## MYSQL DATABASE SETUP
https://dev.mysql.com/downloads/mysql/
https://dev.mysql.com/downloads/workbench/

'default' :{
        'ENGINE' :'django.db.backends.mysql',
        'NAME':'db_lms',
        'PORT':3306,
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':''

    }



## IMPORTANT COMMAND
django-admin --version
django-admin 
