
from django.conf import settings


IS_SMS_ENABLED = getattr(settings, 'IS_SMS_ENABLED', False)

SMS_DB_TABLE_NAME = getattr(settings, 'SMS_DB_TABLE_NAME', '')

SMS_RECIPIENTS = getattr(settings, 'SMS_RECIPIENTS', [])

SMS_SIGNATURE = getattr(settings, 'SMS_SIGNATURE', 'Msg')
