try:
    from importlib import import_module
except ImportError:  # python 2.6
    from django.utils.importlib import import_module

from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import clear_url_caches, reverse, NoReverseMatch

from . import urls


def patch_urlconf():
    try:
        reverse('djgc-chart-data', args=('chart_slug',))
    except NoReverseMatch:
        urlconf_module = import_module(settings.ROOT_URLCONF)

        urlconf_module.urlpatterns = [
            url(r'', include(urls)),
        ] + urlconf_module.urlpatterns

        clear_url_caches()
