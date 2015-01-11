from setuptools import setup, find_packages

setup(
    name="django-google-charts",
    version="0.1.6",
    author="Dan Palmer",
    author_email="dan@danpalmer.me",
    packages=find_packages(exclude=['tests']),
    url='http://danpalmer.me/projects/django-google-charts',
    description="A simple Python interface to Google Charts.",
    include_package_data=True,
)
