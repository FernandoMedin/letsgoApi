import os
import json
import requests
from django.conf import settings
from app.models import User, Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class FaceBook(APIView):

    # POST => /auth/facebook/
    def post(self, request):

        access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token'
        graph_api_url = 'https://graph.facebook.com/v2.3/me'

        params = {
            'client_id': request.data['clientId'],
            'redirect_uri': request.data['redirectUri'],
            'client_secret': settings.FACEBOOK_SECRET,
            'code': request.data['code'],
        }

        r = requests.post(access_token_url, params)
        access_token = json.loads(r.text)

        # GET => https://graph.facebook.com/v2.3/me 
        # to get user profile (email, first_name, last_name, gender, id)
        r = requests.get(graph_api_url, params=access_token)
        profile = json.loads(r.text)

        # Check if email exists
        user = User.objects.filter(email=profile['email']).first()
        if not user:
            # User doesn't exists, Create user model
            name = profile['first_name'].replace(' ', '').lower()
            user = User(email=profile['email'],
                        first_name=profile['first_name'],
                        last_name=profile['last_name'])
            user.save()

            user_profile = Profile(owner=user,
                                facebook_id=profile['id'],
                                facebook_token=access_token['access_token'])
            user_profile.save()
        else:
            # User Exists
            user_connected = Profile.objects.filter(facebook_id=profile['id']).first()
            if not user_connected:
                # create profile with facebook_token
                user_profile = Profile(owner=user,
                                    facebook_id=profile['id'],
                                    facebook_token=access_token['access_token'])
                user_profile.save()

            user.first_name = profile['first_name']
            user.last_name  = profile['last_name']
            user.save()

        # Create token for user
        token, created = Token.objects.get_or_create(user=user)

        data = {
            'token': token.key,
        }

        return Response(data)



