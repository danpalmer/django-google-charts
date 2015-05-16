from django_google_charts.utils import OptionsDict


def test_dot_access():
    key, value = 'key', 'value'
    options = OptionsDict({key: value})

    assert options.key == value

    options2 = OptionsDict()
    options2.key = value

    assert options2.key == value


def test_options_equality():
    options = OptionsDict({'key1': 'value', 'key2': 3})
    test = {'key1': 'value', 'key2': 3}

    assert options == test


def test_adding_dict():
    value = 'value'
    options = OptionsDict()

    options.x = {}
    options.x.y = value

    assert options.x.y == value


def test_options_inherit():
    options = OptionsDict({'overridden': 1, 'kept': 1})
    suboptions = OptionsDict({'overridden': 2, 'new': 1})

    suboptions.inherit(options)

    assert suboptions == {
        'overridden': 2,
        'new': 1,
        'kept': 1,
    }


def test_options_recursive_inherit():
    options = OptionsDict({
        'key': {
            'subkey': {'subsubkey': 2},
        },
    })

    options.inherit(OptionsDict({
        'key': {
            'subkey': {'subsubkey': 1},
            'kept': 1,
        },
    }))

    assert options == {
        'key': {
            'subkey': {'subsubkey': 2},
            'kept': 1,
        },
    }
