from django.apps import AppConfig


class TestbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testb'
    def ready(self):
        import testb.signals
