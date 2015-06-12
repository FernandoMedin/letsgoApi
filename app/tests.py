import json
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

class UserTest(APITestCase):


    def test_get_users(self):
        """
        Should do a request on users API and return 200 status
        """
        # token = Token.objects.get(user__username='FXCesinha')
        # print token.key
        # header = {'Authorization': 'Token 00f22afc6092d390b52076f24bd489aec5462874'}
        # client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token 00f22afc6092d390b52076f24bd489aec5462874')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_user(self):
        # """
        # Should insert a user on database and return 201 status
        # """
        # user = {
            # 'username': 'usernameTest',
            # 'email': 'test@gmail.com'
        # }
        # response = self.client.post('/users/', user)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_user_error(self):
        # """
        # Should create a user with invalid params and return a 400 bad request
        # """
        # user = {
            # 'username_error' : "TestToken"
        # }
        # response = self.client.post('/users/', user)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

