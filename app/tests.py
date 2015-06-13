import datetime
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
        # Authorization header test
        # token = Token.objects.get(user__username='FXCesinha')
        # self.client.credentials(HTTP_AUTHORIZATION='Token 643b0e16920d6bffb77680646a9f909019a17192')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Should insert an user on database and return 201 status
        """
        user = {
            'email': 'test@gmail.com'
        }
        response = self.client.post('/users/', user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_error(self):
        """
        Should create an user with invalid params and return a 400 bad request
        """
        user = {
            'email_error' : "TestToken@gmail.com"
        }
        response = self.client.post('/users/', user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_organization(self):
        """
        Should create an user following by an organization
        """
        user = {
            'email': 'UserToOrg@gmail.com'
        }
        response = self.client.post('/users/', user)
        org = {
            'user': response.data['id'],
            'name': 'org_test',
            'premium': False
        }
        response = self.client.post('/organizations/', org)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_user(self):
        """
        Should create an event by an user
        """
        user = {
            'email': 'UserEvent@gmail.com'
        }
        response = self.client.post('/users/', user)

        event_type = {
            'name': 'private'
        }
        event_type_response = self.client.post('/event_type/', event_type)

        event_category = {
            'name': 'party'
        }
        event_category_response = self.client.post('/event_category/', event_category)
        event = {
            'name': 'EventTest',
            'date': str(datetime.date.today() + datetime.timedelta(days=1)),
            'place': 'SP',
            'time': str(datetime.datetime.now().time()),
            'price': '40.00',
            'user': response.data['id'],
            'organization': None,
            'event_type': event_type_response.data['id'],
            'category': event_category_response.data['id'],
        }
        response = self.client.post('/events/', event)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_event_org(self):
        """
        Should create an event by an org
        """
        user = {
            'email': 'UserEvent2@gmail.com'
        }
        response = self.client.post('/users/', user)

        org = {
            'user': response.data['id'],
            'name': 'orgEvent'
        }
        org_response = self.client.post('/organizations/', org)

        event_type = {
            'name': 'public'
        }
        event_type_response = self.client.post('/event_type/', event_type)

        event_category = {
            'name': 'sport'
        }
        event_category_response = self.client.post('/event_category/', event_category)
        event = {
            'name': 'EventTest',
            'date': str(datetime.date.today() + datetime.timedelta(days=1)),
            'place': 'SP',
            'time': str(datetime.datetime.now().time()),
            'price': '40.00',
            'user': None,
            'organization': org_response.data['id'],
            'event_type': event_type_response.data['id'],
            'category': event_category_response.data['id']
        }
        response = self.client.post('/events/', event)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_event_both(self):
        """
        Should create an event with an user and an organizations with throw an 400 exception
        """
        user = {
            'email': 'UserEvent2@gmail.com'
        }
        response = self.client.post('/users/', user)

        org = {
            'user': response.data['id'],
            'name': 'orgEvent'
        }
        org_response = self.client.post('/organizations/', org)

        event_type = {
            'name': 'public'
        }
        self.client.post('/event_type/', event_type)

        event_category = {
            'name': 'sport'
        }
        self.client.post('/event_category/', event_category)
        event = {
            'name': 'EventTest',
            'date': str(datetime.date.today() + datetime.timedelta(days=1)),
            'place': 'SP',
            'time': str(datetime.datetime.now().time()),
            'price': '40.00',
            'user': response.data['id'],
            'organization': org_response.data['id'],
            'event_type': '1',
            'category': '1',
        }
        response = self.client.post('/events/', event)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
