
from django.apps import apps
from django.template.loader import render_to_string

from turbosms.settings import IS_SMS_ENABLED, SMS_RECIPIENTS
from turbosms.models import SMS


def get_default_sms_recipients():

    if apps.is_installed('site_config'):
        from site_config import config
        return getattr(config, 'SMS_RECIPIENTS', SMS_RECIPIENTS)

    return SMS_RECIPIENTS


def send_sms(message, recipients=None):

    if not IS_SMS_ENABLED:
        return

    if recipients is None:
        recipients = get_default_sms_recipients()

    for number in recipients:
        SMS.objects.create(number=number, message=message)


def send_sms_from_template(template_name, context=None):
    message = render_to_string(template_name, context)
    send_sms(message)
