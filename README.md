# MP-TurboSMS

Python/Django app for SQL api of turbosms.ua https://turbosms.ua/sql.html

### Installation

Install with pip:

```sh
$ pip install django-turbosms
```

Add turbosms to settings.py:
```
IS_SMS_ENABLED = True

INSTALLED_APPS = [
    'turbosms',
]

DATABASE_ROUTERS = ['turbosms.routers.TurboSMSRouter']
SMS_DB_TABLE_NAME = ''
SMS_RECIPIENTS = [] # Can be set using mp-config app

DATABASES = {
    ...,
    'turbosms': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users',
        'USER': '',
        'PASSWORD': '',
        'HOST': '94.249.146.189',
        'PORT': ''
    }
}
```
