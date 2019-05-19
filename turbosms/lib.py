
from django.apps import apps
from django.db import connections
from django.template.loader import render_to_string

from turbosms import settings


def get_default_sms_recipients():

    if apps.is_installed('site_config'):
        from site_config import config
        return getattr(config, 'SMS_RECIPIENTS', settings.SMS_RECIPIENTS)

    return settings.SMS_RECIPIENTS


def send_sms(message, recipients=None):

    if not settings.IS_SMS_ENABLED:
        return

    if recipients is None:
        recipients = get_default_sms_recipients()

    query = (
        'INSERT INTO {} (number, message, sign) VALUES (%s, %s, %s)'
    ).format(settings.SMS_DB_TABLE_NAME)

    with connections['turbosms'].cursor() as cursor:
        for number in recipients:
            cursor.execute(query, [
                number,
                message,
                settings.SMS_SIGNATURE])


def send_sms_from_template(template_name, context=None, recipients=None):
    message = render_to_string(template_name, context)
    send_sms(message, recipients)
