
from django.conf import settings
from django.db import connections
from django.template.loader import render_to_string


def get_default_sms_recipients():

    try:
        from site_config import config
        return config.SMS_RECIPIENTS
    except (ImportError, AttributeError):
        pass

    return getattr(settings, 'SMS_RECIPIENTS', [])


def send_sms(message, recipients=None):

    if not getattr(settings, 'IS_SMS_ENABLED', False):
        return

    if recipients is None:
        recipients = get_default_sms_recipients()

    query = (
        'INSERT INTO {} (number, message, sign) VALUES (%s, %s, %s)'
    ).format(settings.SMS_USERNAME)

    with connections['turbosms'].cursor() as cursor:
        for number in recipients:
            cursor.execute(query, [
                number,
                message,
                getattr(settings, 'SMS_SIGNATURE', 'Msg')])


def send_sms_from_template(template_name, context=None, recipients=None):
    message = render_to_string(template_name, context)
    send_sms(message, recipients)
