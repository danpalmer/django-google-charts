import json

from django.utils.html import format_html
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Chart(object):
    options = {}
    chart_slug = None
    columns = None

    def get_data(self):
        raise NotImplementedError

    def slug(self):
        return str(hash(self))

    def __str__(self):
        return format_html(
            "<div "
                "data-chart-options='{0}'"
            "></div>",
            json.dumps(self.options),
        )
