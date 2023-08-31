# Python HTTP api for TurboSMS
https://turbosms.ua/ua/api.html

### Installation

```
pip install django-turbosms
```

settings.py:
```
IS_SMS_ENABLED = True
SMS_SIGNATURE = 'MySender'
SMS_TOKEN = '*****************'
SMS_RECIPIENTS = [] # Can be set using mp-config app

INSTALLED_APPS = [
    ...
    'turbosms',
]
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
