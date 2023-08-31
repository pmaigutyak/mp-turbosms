from django.core.management.base import BaseCommand
from turbosms.lib import send_sms


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_sms('test', debug=True)
        self.stdout.write(self.style.SUCCESS('Success'))
