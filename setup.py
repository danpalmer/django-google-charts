from distutils.core import setup

setup(
    name="django-google-charts",
    version="0.1.2",
    author="Dan Palmer",
    author_email="dan@danpalmer.me",
    packages=[
        'django_google_charts',
        'django_google_charts.templatetags',
    ],
    url='http://danpalmer.me/projects/django-google-charts',
    description="A simple Python interface to Google Charts.",
)
