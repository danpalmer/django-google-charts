from django_google_charts.templatetags import django_google_charts


def test_template_tag_resources(self):
    html = django_google_charts.django_google_chart_js()
