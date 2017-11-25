from setuptools import setup, find_packages

setup(
    name = "django-allauth-microsoft",
    version = "0.0.1",
    author = "Vincent Schaenzer",
    author_email = "vincent@schaenzer.com",
    description = "Microsoft OAuth2 provider for django-allauth",
    url = "https://github.com/schaenzer/django-allauth-microsoft",
    packages=find_packages(),
    install_requires=['django-allauth>=0.34.0'],
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
