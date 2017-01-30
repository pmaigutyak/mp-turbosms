
from django.contrib import admin

from turbosms.models import SMSRecord


class SMSRecordAdmin(admin.ModelAdmin):

    list_display = [
        'number', 'message', 'cost', 'balance', 'msg_id', 'sended', 'status'
    ]
    search_fields = ['number', 'message', 'msg_id']

    def has_add_permission(self, request):
        return False


admin.site.register(SMSRecord, SMSRecordAdmin)
