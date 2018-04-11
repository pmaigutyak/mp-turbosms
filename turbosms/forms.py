
from django import forms

from turbosms.models import SMSTemplate


class SendSMSForm(forms.ModelForm):

    def clean_recipients(self):
        recipients = self.cleaned_data['recipients'] or None

        if recipients is not None:
            recipients = recipients\
                .replace(' ', '')\
                .replace('\r', '')\
                .split('\n')

        return recipients

    class Meta:
        model = SMSTemplate
        fields = ['recipients', 'text']
