from django.apps import AppConfig

from .settings import patch_urlconf


class ChartsConfig(AppConfig):
    name = 'django_google_charts'
    verbose_name = "Django Google Charts"

    def ready(self):
        patch_urlconf()
