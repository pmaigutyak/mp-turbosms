
from django.db import models
from django.utils.translation import ugettext_lazy as _

from turbosms.config import SMS_USERNAME, SMS_SIGNATURE


class SMS(models.Model):

    number = models.CharField(max_length=21)

    sign = models.CharField(max_length=21, default=SMS_SIGNATURE)

    message = models.TextField(max_length=1530)

    wappush = models.CharField(max_length=128)

    is_flash = models.BooleanField(default=False)

    msg_id = models.CharField(max_length=36, blank=True)

    cost = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    added = models.DateTimeField(blank=True)

    send_time = models.DateTimeField(blank=True)

    sended = models.DateTimeField(blank=True)

    received = models.DateTimeField(blank=True)

    error_code = models.CharField(max_length=3, blank=True)

    status = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _('SMS record')
        verbose_name_plural = _('SMS Records')
        db_table = SMS_USERNAME
