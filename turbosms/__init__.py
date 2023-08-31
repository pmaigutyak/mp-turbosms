import requests

from django.conf import settings
from django.template.loader import render_to_string


def get_default_sms_recipients():

    try:
        from site_config import config
        recipients = config.SMS_RECIPIENTS
    except Exception:
        recipients = None

    return recipients or getattr(settings, 'SMS_RECIPIENTS', [])


def send_sms(message, recipients=None, debug=False):

    if not getattr(settings, 'IS_SMS_ENABLED', False):
        if debug:
            raise Exception("settings.IS_SMS_ENABLED is not True")
        return

    if not getattr(settings, 'SMS_TOKEN'):
        if debug:
            raise Exception("settings.SMS_TOKEN is undefined")
        return

    if recipients is None:
        recipients = get_default_sms_recipients()

    if not recipients:
        if debug:
            raise Exception("no recipients found")
        return

    response = requests.post(
        url=(
            'https://api.turbosms.ua/message/send.json?token=%s' %
            settings.SMS_TOKEN
        ),
        json={
            "recipients": recipients,
            "sms": {
                "sender": getattr(settings, 'SMS_SIGNATURE', 'Msg'),
                "text": message
            }
        }
    )

    if response.status_code != 200 and debug:
        raise Exception(response.content)


def send_sms_from_template(template_name, context=None, recipients=None):
    message = render_to_string(template_name, context)
    send_sms(message, recipients)
