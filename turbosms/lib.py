
from django.apps import apps
from django.template import Template, Context
from django.template.loader import render_to_string

from turbosms.settings import IS_SMS_ENABLED, SMS_RECIPIENTS
from turbosms.models import SMS, SMSTemplate
from turbosms.exceptions import SMSTemplateDoesNotExist


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
    send_sms(render_to_string(template_name, context))


def send_sms_from_template_record(slug, context=None, recipients=None):

    try:
        sms_template = SMSTemplate.objects.get(slug=slug)
    except SMSTemplate.DoesNotExist:
        raise SMSTemplateDoesNotExist('SMS template not found: %s' % slug)

    template = Template(sms_template.text)

    if recipients is None:
        recipients = sms_template.get_recipients()

    send_sms(template.render(Context(context)), recipients)
