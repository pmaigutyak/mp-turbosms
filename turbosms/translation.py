
from modeltranslation.translator import translator, TranslationOptions

from turbosms.models import SMSTemplate


class SMSTemplateTranslationOptions(TranslationOptions):
    fields = ['text']


translator.register(SMSTemplate, SMSTemplateTranslationOptions)
