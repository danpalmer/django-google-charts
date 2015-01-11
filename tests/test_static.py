from django.contrib.staticfiles.storage import staticfiles_storage


def test_static_url():
    chart_js_url = staticfiles_storage.url('django_google_charts/charts.js')

    assert chart_js_url == '/static/django_google_charts/charts.js'
