
from django.template.loader import render_to_string

from mpsite.sms.settings import IS_SMS_ENABLED, SMS_RECIPIENTS
from mpsite.sms.models import SMS


def send_sms(message):

    if IS_SMS_ENABLED:
        for number in SMS_RECIPIENTS:
            SMS.objects.create(number=number, message=message)


def send_sms_from_template(template_name, context=None):
    message = render_to_string(template_name, context)
    send_sms(message)
