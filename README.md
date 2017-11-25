# django-allauth-microsoft
Microsoft OAuth2 provider for django-allauth

## Installation

### requirements
* django-allauth (https://github.com/pennersr/django-allauth)

### python package
```
pip install django-allauth-microsoft
```
### settings.py

The {tenant} value in the path of the request can be used to control who can sign into the application. The allowed values are tenant identifiers, for example, 8eaef023-2b34-4da1-9baa-8bc8c9d6a490 or contoso.onmicrosoft.com or common for tenant-independent tokens

```
INSTALLED_APPS = (
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
     ...
     # Add allauth_microsoft to installed_apps
   	'allauth_microsoft'
     ...
)

SOCIALACCOUNT_PROVIDERS = {
    'microsoft': {
        'TENANT': '{tenant}',
    }
}

# Useful settings
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'none'
```
## Post-Installation

### register your application
* Create your application on [https://apps.dev.microsoft.com/](https://apps.dev.microsoft.com/)
* Callback is  http://{hostname}/accounts/microsoft/login/callback/
* Copy your Application Id
* Create and Copy Application Secrets

Add Application Id Secrets as social application in django admin.

## Contributors
* Vincent Schänzer (vincent@schaenzer.com)
* Modell Aachen GmbH ([www.modell-aachen.de](www.modell-aachen.de))
* Thanks to Lamelos for his [django-allauth-office365](https://github.com/Lamelos/django-allauth-office365/tree/master/allauth_office365)

## License
[MIT License](https://github.com/schaenzer/django-allauth-microsoft/blob/master/LICENSE)
