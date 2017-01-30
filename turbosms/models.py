
from django.db import models
from django.utils.translation import ugettext_lazy as _

from turbosms.settings import SMS_DB_TABLE_NAME, SMS_SIGNATURE


class SMS(models.Model):

    number = models.CharField(max_length=21)

    sign = models.CharField(max_length=21, default=SMS_SIGNATURE)

    message = models.TextField(max_length=1530)

    wappush = models.CharField(max_length=128)

    is_flash = models.BooleanField(default=False)

    class Meta:
        db_table = SMS_DB_TABLE_NAME


class SMSRecord(models.Model):

    msg_id = models.CharField(max_length=36)

    number = models.CharField(max_length=21)

    sign = models.CharField(max_length=21, default=SMS_SIGNATURE)

    message = models.TextField(max_length=1530)

    wappush = models.CharField(max_length=128)

    is_flash = models.BooleanField(default=False)

    cost = models.DecimalField(max_digits=4, decimal_places=2)

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    added = models.DateTimeField()

    send_time = models.DateTimeField()

    sended = models.DateTimeField()

    received = models.DateTimeField()

    error_code = models.CharField(max_length=3)

    status = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('SMS record')
        verbose_name_plural = _('SMS Records')
        db_table = SMS_DB_TABLE_NAME
