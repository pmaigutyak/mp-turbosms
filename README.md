# MP-TurboSMS

Python/Django app for SQL api of turbosms.ua https://turbosms.ua/sql.html

### Installation

Install with pip:

```sh
pip install django-turbosms
```

Add turbosms to settings.py:
```
IS_SMS_ENABLED = True

INSTALLED_APPS = [
    'turbosms',
]

DATABASE_ROUTERS = ['turbosms.routers.TurboSMSRouter']
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

### Usage
```
>>> from turbosms import send_sms, send_sms_from_template, get_default_sms_recipients

# recipients param is optional (default: settings.SMS_RECIPIENTS)
>>> send_sms('sms message', recipients=['+38096*******])

# context param is optional (dafault: {})
# recipients param is optional (default: settings.SMS_RECIPIENTS)
>>> send_sms_from_template('sms.txt', context={'example': 'example'}, recipients=['+38096*******])

# returns default sms recipients from config
>>> get_default_sms_recipients()
```
