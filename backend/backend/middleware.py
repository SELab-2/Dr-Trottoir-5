import requests
from django.conf import settings

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError


class RefreshMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        new_access_token = None
        valid_access_token = True

        if request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) is None:
            valid_access_token = False
        else:
            try:  # check if access token is still valid
                AccessToken(request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']))
            except TokenError:
                valid_access_token = False

        if not valid_access_token:
            if request.COOKIES.get(settings.SIMPLE_JWT['REFRESH_COOKIE']) is not None:
                try:  # check if the refresh token is valid
                    refresh = RefreshToken(request.COOKIES.get(settings.SIMPLE_JWT['REFRESH_COOKIE']))
                    # refresh the access token
                    new_access_token = requests.post('http://localhost:8000/api/refresh/', data={'refresh': refresh}).json()['access']
                    # add the access token to the request
                    request.COOKIES[settings.SIMPLE_JWT['AUTH_COOKIE']] = new_access_token
                except TokenError:
                    pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if new_access_token is not None:
            # send the new access token cookie back to the browser
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=new_access_token,
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
        return response
