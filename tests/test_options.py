from django_google_charts.utils import OptionsDict


def test_dot_access(self):
    key, value = 'key', 'value'
    options = OptionsDict({key: value})

    self.assertEqual(options.key, value)

    options2 = OptionsDict()
    options2.key = value

    self.assertEqual(options2.key, value)


def test_options_equality(self):
    options = OptionsDict({'key1': 'value', 'key2': 3})
    test = {'key1': 'value', 'key2': 3}

    self.assertEqual(options, test)


def test_adding_dict(self):
    value = 'value'
    options = OptionsDict()

    options.x = {}
    options.x.y = value

    self.assertEqual(options.x.y, value)


def test_options_merge(self):
    options = OptionsDict({'overridden': 1, 'kept': 1})
    suboptions = OptionsDict({'overridden': 2, 'new': 1})

    options.merge(suboptions)

    self.assertEqual(options, {
        'overridden': 2,
        'new': 1,
        'kept': 1,
    })


def test_options_recursive_merge(self):
    options = OptionsDict({
        'key': {
            'subkey': {'subsubkey': 1},
            'kept': 1,
        },
    })

    options.merge(OptionsDict({
        'key': {
            'subkey': {'subsubkey': 2},
        },
    }))

    self.assertEqual(options, {
        'key': {
            'subkey': {'subsubkey': 2},
            'kept': 1,
        },
    })
