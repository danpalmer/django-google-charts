from django.conf.urls import patterns, include, url

from .views import chart_data

urlpatterns = patterns('',
    url(
        r'^chart/(?P<chart_slug>[\w\.]+)/?$',
        chart_data,
        name='djgc-chart-data',
    ),
)
