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


class OptionsDict(dict):

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, attr):
        value = self.get(attr)

        if isinstance(value, dict):
            value = OptionsDict(value)
            self[attr] = value

        return value

    def inherit(self, new):
        iterator = new.items()
        self.recursive_inherit(iterator)

    def recursive_inherit(self, iterator):
        for (key, value) in iterator:
            if (
                key in self
                and isinstance(self[key], dict) and isinstance(value, dict)
            ):
                self[key] = OptionsDict(self[key])
                self[key].inherit(value)
            elif key not in self:
                self[key] = value
