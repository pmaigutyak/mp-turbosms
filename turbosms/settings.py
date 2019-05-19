
from django.conf import settings


IS_SMS_ENABLED = getattr(settings, 'IS_SMS_ENABLED', False)

SMS_RECIPIENTS = getattr(settings, 'SMS_RECIPIENTS', [])

SMS_SIGNATURE = getattr(settings, 'SMS_SIGNATURE', 'Msg')

try:
    SMS_DB_TABLE_NAME = settings.DATABASES['turbosms']['USER']
except KeyError:
    SMS_DB_TABLE_NAME = ''
