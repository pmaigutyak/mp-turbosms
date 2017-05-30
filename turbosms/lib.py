
from django.apps import apps
from django.template.loader import render_to_string

from turbosms.settings import IS_SMS_ENABLED, SMS_RECIPIENTS
from turbosms.models import SMS


def get_recipients():

    if apps.is_installed('site_config'):

        from site_config import config

        if hasattr(config, 'SMS_RECIPIENTS'):
            return config.SMS_RECIPIENTS

    return SMS_RECIPIENTS


def send_sms(message):

    if IS_SMS_ENABLED:
        for number in get_recipients():
            SMS.objects.create(number=number, message=message)


def send_sms_from_template(template_name, context=None):
    message = render_to_string(template_name, context)
    send_sms(message)
