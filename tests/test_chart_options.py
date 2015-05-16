from django_google_charts.utils import OptionsDict
from django_google_charts.charts import Chart

KEY, VALUE, OVERRIDE = 'key', 'value', 'override'


class SuperChart(Chart):
    options = {KEY: VALUE}


class SubChart1(SuperChart):
    options = {'other_key': 'other_value'}


class SubChart2(SuperChart):
    options = {KEY: OVERRIDE}


def test_chart_options_wrapped():
    chart = SuperChart()
    assert isinstance(chart.options, OptionsDict)


def test_chart_inherits_options():
    subchart = SubChart1()
    assert subchart.options[KEY] == VALUE


def test_chart_overrides_superclass_options():
    subchart = SubChart2()
    assert subchart.options[KEY] == OVERRIDE
