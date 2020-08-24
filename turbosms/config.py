
from django.conf import settings

from turbosms import defaults


IS_SMS_ENABLED = getattr(settings, 'IS_SMS_ENABLED', defaults.IS_SMS_ENABLED)

SMS_RECIPIENTS = getattr(settings, 'SMS_RECIPIENTS', defaults.SMS_RECIPIENTS)

SMS_SIGNATURE = getattr(settings, 'SMS_SIGNATURE', defaults.SMS_SIGNATURE)

SMS_USERNAME = getattr(settings, 'SMS_USERNAME', '')
