
class TurboSMSRouter(object):

    app_label = 'turbosms'
    db_name = 'turbosms'
    related_models = ['sms', 'smsrecord']

    def _is_related_model(self, model):
        return (
            model._meta.app_label == self.app_label and
            model.__name__.lower() in self.related_models
        )

    def db_for_read(self, model, **hints):

        if self._is_related_model(model):
            return self.db_name

        return None

    def db_for_write(self, model, **hints):

        if self._is_related_model(model):
            return self.db_name

        return None

    def allow_relation(self, obj1, obj2, **hints):

        if self._is_related_model(obj1) or self._is_related_model(obj2):
            return False

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == self.app_label and model_name in self.related_models:
            return False

        return None
