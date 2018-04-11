
from turbosms.models import SMSTemplate, SMSRecord


def create_sms_template(
        name='Test template',
        slug='test',
        text='Test message',
        recipients=None):

    return SMSTemplate.objects.create(
        name=name,
        slug=slug,
        text=text,
        recipients=recipients)


def get_sms_records():
    return SMSRecord.objects.all()
