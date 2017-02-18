# MP-TurboSMS

Python/Django app for SQL api of turbosms.ua https://turbosms.ua/sql.html

### Installation

Install with pip:

```sh
$ pip install -e git://github.com/pmaigutyak/mp-turbosms.git#egg=mp-turbosms
```

Add turbosms to settings.py:
```
INSTALLED_APPS = [
    'turbosms',
]

DATABASE_ROUTERS = ['turbosms.routers.TurboSMSRouter']
```
