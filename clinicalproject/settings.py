"""
Django settings for clinicalproject project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#from sqlalchemy import VARCHAR

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uiiy#69xe2%(ska5-_lwvdc!p0$(^-)^xkywttk5oj4#)&#&(b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration_system.apps.RegistrationSystemConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'clinicalproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'clinicalproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    #'default': {
       # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'new',
       # 'USER': 'postgres',
       # 'PASSWORD': '6#8!4KZe',
       # 'HOST': 'localhost',
        #'PORT': '',

#import psycopg2

   # }
#conn = psycopg2.connect(
        #database= 'new',
        #user= 'postgres',
       # password= '6#8!4KZe',
        #host= 'localhost',
       # port= '',
#)
#conn.autocommit = True

#cursor = conn.cursor()
#cursor.execute('''SELECT * from Patient''')

#
#result = cursor.fetchall();
#print(result)

#cursor.execute(sql)

#django.db.backends.postgresql_psycopg2
#cursor.execute("select version()")
#cursor.execute("""INSERT INTO Patient_new(ID, First_name, Last_name) VALUES (1, 'ma', 'b')""")

# list that contain records to be inserted into table
# data = [('Babita', 'Bihar'), ('Anushka', 'Hyderabad'),
#         ('Anamika', 'Banglore'), ('Sanaya', 'Pune'),
#         ('Radha', 'Chandigarh')]

# inserting record into employee table
# for d in data:
#     cursor.execute("INSERT into employee(name, state) VALUES (%s, %s)", d)
#
# print("List has been inserted to employee table successfully...")

# Commit your changes in the database
#conn.commit()

# Closing the connection
#conn.close()


}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

static_directories = (os.path.join(BASE_DIR, 'static'),)