# -*- coding: utf-8 -*-
import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter, OAuth2CallbackView, OAuth2LoginView
from .provider import MicrosoftProvider


class MicrosoftAuth2Adapter(OAuth2Adapter):
    provider_id = MicrosoftProvider.id

    settings = app_settings.PROVIDERS.get(provider_id, {})
    tenant = settings.get("TENANT")

    authorize_url = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize".format(tenant=tenant)
    access_token_url = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token".format(tenant=tenant)
    profile_url = "https://graph.microsoft.com/v1.0/me"

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(MicrosoftAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(MicrosoftAuth2Adapter)
