from importd import d


def pytest_configure():
    d(
        SECRET_KEY='secret_key',
        INSTALLED_APPS=(
            'django.contrib.staticfiles',
            'django_google_charts',
        ),
    )
