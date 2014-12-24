import json

from django.utils.html import format_html
from django.utils.encoding import python_2_unicode_compatible

from .utils import DateTimeEncoder


@python_2_unicode_compatible
class Chart(object):
    options = {}
    chart_slug = None
    columns = None

    def get_data(self):
        raise NotImplementedError

    def chart_id(self):
        return str(hash(self))

    def __str__(self):
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
            "></div>",
            self.chart_id(),
            json_data,
            json.dumps(self.options),
        )
