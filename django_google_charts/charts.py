import json

from django.utils.html import format_html, mark_safe

from .utils import DateTimeEncoder


class Chart(object):
    options = {}
    chart_slug = None
    columns = None

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
            "></div>",
            self.chart_id(),
            mark_safe(json_data),
            json.dumps(self.options),
        )

    def __str__(self):
        return self.to_html()

    def __unicode__(self):
        return self.to_html()
