import json
from app.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.authtoken.models import Token
from rest_framework import exceptions, serializers
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

class TokenAuth(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except:
            raise exceptions.AuthenticationFailed('Invalid token')

        return token.user, token


# from https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/authtoken/serializers.py
class TokenSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):

        email    = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs

class ObtainAuthToken(ObtainAuthToken):

    serializer_class = TokenSerializer
    # renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request):
        #TODO: render a view
        return Response()

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)

        return Response({ 'token': token.key })

obtain_expiring_auth_token = ObtainAuthToken.as_view()
