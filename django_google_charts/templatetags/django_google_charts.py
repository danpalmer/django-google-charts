from django import template
from django.utils.html import format_html
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()


def django_google_chart_js():
    chart_js_url = staticfiles_storage.url('django_google_charts/charts.js')

    return format_html(
        """
        <script type="text/javascript"
            src="https://www.google.com/jsapi?autoload={
                {'modules':[{{
                    'name':'visualization',
                    'version':'1',
                    'packages':['corechart']
                }}]}}">
        </script>
        <script type="text/javascript" src="{0}"></script>
        """,
        chart_js_url,
    )

register.simple_tag(django_google_chart_js)
