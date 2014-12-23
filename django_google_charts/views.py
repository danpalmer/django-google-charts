import json

from django.http import HttpResponse

from .utils import DateTimeEncoder
from .charts import CHARTS

def chart_data(request, chart_slug):
    chart = CHARTS[chart_slug]()

    response = HttpResponse()
    response['Content-type'] = 'application/json'

    data = {
        'cols': chart.columns,
        'rows': list(chart.get_data()),
    }

    json.dump(data, response, cls=DateTimeEncoder)

    return response
