import json

from abc import abstractmethod

from django.utils.six import with_metaclass
from django.utils.html import format_html, mark_safe

from .utils import DateTimeEncoder, OptionsDict


class ChartMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'options' in attrs:
            options = OptionsDict(attrs['options'])
            options.inherit(getattr(bases[0], 'options', {}))
            attrs['options'] = options

        return super(ChartMeta, cls).__new__(cls, name, bases, attrs)


class Chart(with_metaclass(ChartMeta, object)):
    options = {}
    columns = None
    chart_type = 'LineChart'

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    def chart_id(self):
        return str(hash(self))

    def to_html(self):
        data = {
            'cols': self.columns,
            'rows': list(self.get_data()),
        }

        json_data = json.dumps(data, cls=DateTimeEncoder)

        return format_html(
            "<script type='text/json' id='{0}'>{1}</script>"
            "<div "
                "data-chart-options='{2}'"
                "data-chart-id='{0}'"
                "data-chart-type='{3}'"
            "></div>",
            self.chart_id(),
            mark_safe(json_data),
            json.dumps(self.options),
            self.chart_type,
        )

    def __str__(self):
        return self.to_html()

    def __unicode__(self):
        return self.to_html()


# class ComboChart(Chart):
#     chart_type = 'ComboChart'


class LineChart(Chart):
    chart_type = 'LineChart'


class GeoChart(Chart):
    chart_type = 'GeoChart'


class CoreChart(Chart):
    chart_type = 'CoreChart'


class AreaChart(Chart):
    chart_type = 'AreaChart'


class BarChart(Chart):
    chart_type = 'BarChart'


class BubbleChart(Chart):
    chart_type = 'BubbleChart'


class CandlestickChart(Chart):
    chart_type = 'CandlestickChart'


class Histogram(Chart):
    chart_type = 'Histogram'


class ColumnChart(Chart):
    chart_type = 'ColumnChart'


class PieChart(Chart):
    chart_type = 'PieChart'


class ScatterChart(Chart):
    chart_type = 'ScatterChart'


class SparklineChart(Chart):
    chart_type = 'SparklineChart'


class SteppedAreaChart(Chart):
    chart_type = 'SteppedAreaChart'
