from django.apps import AppConfig


class PublicConfig(AppConfig):
    name = 'bitcoin_designed.public'
    verbose_name = 'Public'

    def ready(self):
        pass
