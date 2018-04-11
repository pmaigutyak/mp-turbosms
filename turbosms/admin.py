
from importlib import import_module

from django.apps import apps
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404, render, redirect

from turbosms.models import SMSRecord, SMSTemplate
from turbosms.forms import SendSMSForm
from turbosms.lib import send_sms


def _get_sms_template_admin_base_class():

    if apps.is_installed('modeltranslation'):
        return import_module('modeltranslation.admin').TranslationAdmin

    return admin.ModelAdmin


class SMSRecordAdmin(admin.ModelAdmin):

    list_display = [
        'number', 'message', 'cost', 'balance', 'msg_id', 'sended', 'status'
    ]
    search_fields = ['number', 'message', 'msg_id']

    def has_add_permission(self, request):
        return False


class SMSTemplateAdmin(_get_sms_template_admin_base_class()):

    list_display = ['name', 'slug', 'send_sms_link']
    search_fields = ['name', 'slug', 'recipients', 'text']

    def get_readonly_fields(self, request, obj=None):
        return ['placeholders'] if obj else []

    def send_sms_link(self, item):
        html = """
            <a class="btn btn-primary btn-block pull-right" href="%s">
                <i class="fa fa-upload"></i> %s
            </a>
        """
        return html % (
            reverse_lazy('admin:send-sms', args=[item.id]), _('Send'))

    send_sms_link.short_description = _('Actions')
    send_sms_link.allow_tags = True

    def get_urls(self):

        return [
            url(r'^(.+)/send/$', self.send_sms_template, name='send-sms'),
        ] + super(SMSTemplateAdmin, self).get_urls()

    def send_sms_template(self, request, object_id):

        template = get_object_or_404(SMSTemplate, pk=object_id)

        form = SendSMSForm(request.POST or None, instance=template)

        if request.method == 'POST' and form.is_valid():
            data = form.cleaned_data
            send_sms(data['text'], data['recipients'])
            messages.success(request, _('SMS was sent'))
            return redirect('admin:turbosms_smstemplate_changelist')

        return render(request, 'turbosms/send_sms.html', {'form': form})


admin.site.register(SMSRecord, SMSRecordAdmin)
admin.site.register(SMSTemplate, SMSTemplateAdmin)
