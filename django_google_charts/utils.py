import json
import calendar
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):

        # Serialise DateTimes to a number of milliseconds to be parsed in JS
        if isinstance(obj, datetime.datetime):
            if obj.utcoffset() is not None:
                obj = obj - obj.utcoffset()

            encoded_object = int(
                calendar.timegm(obj.timetuple()) * 1000 +
                obj.microsecond / 1000
            )

        # If a Date, serialise to YYYY-MM-DD to be parsed in JS
        elif isinstance(obj, datetime.date):
            encoded_object = obj.strftime("%Y-%m-%d")

        else:
            encoded_object = json.JSONEncoder.default(self, obj)

        return encoded_object