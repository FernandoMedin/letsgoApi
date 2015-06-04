from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

class UserTest(APITestCase):

    def test_get_users(self):
        """
        Should do a request on users API and return 200 status
        """
        response = self.client.get('/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Should insert a user on database and return 201 status
        """
        user = {
            'facebook_token' : "TestToken"
        }
        response = self.client.post('/users/', user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_error(self):
        """
        Should create a user with invalid params and return a 400 bad request
        """
        user = {
            'facebook_token_invalid' : "TestToken"
        }
        response = self.client.post('/users/', user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

