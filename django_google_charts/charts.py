import json

from django.utils import six
from django.utils.html import format_html, mark_safe
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

CHARTS = {}

class ChartMeta(type):
    def __new__(cls, name, bases, attrs):
        klass = super(ChartMeta, cls).__new__(cls, name, bases, attrs)

        if klass.chart_slug:
            CHARTS[klass.chart_slug] = klass

        return klass

@six.add_metaclass(ChartMeta)
@python_2_unicode_compatible
class Chart(object):
    options = {}
    chart_slug = None
    columns = None

    def get_data(self):
        raise NotImplementedError

    def __str__(self):
        return format_html(
            "<div "
              "data-chart-options='{0}'"
              "data-chart-url='{1}'"
            "></div>",
            json.dumps(self.options),
            reverse(
                'djgc-chart-data',
                args=(self.chart_slug,),
            ),
        )