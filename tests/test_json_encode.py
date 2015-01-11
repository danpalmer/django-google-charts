import json
import datetime

from django_google_charts.utils import DateTimeEncoder


def test_datetime_encoding():
    obj = {'datetime': datetime.datetime(2015, 1, 2, 3, 4, 5)}
    json_str = json.dumps(obj, cls=DateTimeEncoder)

    assert '1420167845000' in json_str


def test_date_encoding():
    obj = {'datetime': datetime.date(2015, 1, 2)}
    json_str = json.dumps(obj, cls=DateTimeEncoder)

    assert '2015-01-02' in json_str
