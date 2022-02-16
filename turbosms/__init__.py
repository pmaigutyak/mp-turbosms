
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_settings(settings, is_prod, **kwargs):

    settings['DATABASE_ROUTERS'] += ['turbosms.routers.TurboSMSRouter']

    if settings.get('IS_SMS_ENABLED'):
        settings['DATABASES']['turbosms'] = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'users',
            'USER': settings.get('SMS_USERNAME'),
            'PASSWORD': settings.get('SMS_PASSWORD'),
            'HOST': '94.249.146.189',
            'PORT': ''
        }


class TurboSMSConfig(AppConfig):
    name = 'turbosms'
    verbose_name = _("Turbosms")


default_app_config = 'turbosms.TurboSMSConfig'
