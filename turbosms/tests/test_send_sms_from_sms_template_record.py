
from django.test import TestCase
from django.core.management import call_command

from turbosms.tests.helpers import create_sms_template, get_sms_records
from turbosms.lib import send_sms_from_template_record


class SendSMSFromTemplateRecordTest(TestCase):

    def setUp(self):
        call_command('sync_translation_fields', interactive=False)

    def test_method_sends_sms(self):

        create_sms_template()

        send_sms_from_template_record('test')

        records = get_sms_records()

        print records
