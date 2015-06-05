from django.db import models
from app.models import Users
import datetime


class UsersModels(models.Model):

    def insert_user(self, token, name, last_name, email):
        if token:
            response = Users(
                token=token,
                name=name,
                last_name=last_name,
                email=email,
                created_at=datetime.datetime.now())
            response.save()

            return True

        return False

    def login_facebook(self, token):

        response = ""

        if token:
            response = Users.objects.get(token=token)

        if response:
            return True

        return False
