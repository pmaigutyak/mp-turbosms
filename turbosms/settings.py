
from turbosms import defaults


class TurboSMSSettings(object):

    IS_SMS_ENABLED = defaults.IS_SMS_ENABLED
    SMS_RECIPIENTS = defaults.SMS_RECIPIENTS
    SMS_SIGNATURE = defaults.SMS_SIGNATURE
    SMS_USERNAME = ''
    SMS_PASSWORD = ''

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'turbosms'
        ]

    @property
    def DATABASES(self):
        databases = super().DATABASES

        if self.IS_SMS_ENABLED:
            databases['turbosms'] = {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'users',
                'USER': self.SMS_USERNAME,
                'PASSWORD': self.SMS_PASSWORD,
                'HOST': '94.249.146.189',
                'PORT': ''
            }

        return databases

    @property
    def DATABASE_ROUTERS(self):
        return super().DATABASE_ROUTERS + [
            'turbosms.routers.TurboSMSRouter'
        ]


default = TurboSMSSettings
