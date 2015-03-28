import re
import json

from django.utils.safestring import SafeString

from django_google_charts.charts import Chart

TEST_DATA = [1, 2]


class TestChart(Chart):

    def get_data(self):
        return TEST_DATA


def test_chart_data_rendering():
    chart = TestChart()
    chart_html = chart.to_html()

    assert json.dumps(TEST_DATA) in chart_html


def test_chart_element_rendering():
    chart = TestChart()
    chart_html = chart.to_html()

    assert re.search(r'data-chart-id=\'.+?\'', chart_html)


def test_chart_type():
    chart = TestChart()
    chart.chart_type = 'SteppedAreaChart'
    chart_html = chart.to_html()

    assert re.search(r'data-chart-type=\'SteppedAreaChart\'', chart_html)


def test_chart_safe_string():
    chart = TestChart()
    chart_html = chart.to_html()

    assert isinstance(chart_html, SafeString)
