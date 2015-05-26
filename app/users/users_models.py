from django.db import models
from app.models import Users
import datetime

class UsersModels(models.Model):

    def insert_token(self, token):
        if token:
            response = Users(
                    token=token,
                    created_at=datetime.datetime.now())
            response.save()

            return 1

        return 0

    def login_facebook(self, token):

        response = ""

        if token:
            response = Users.objects.get(token=token)

        if response:
            return 1

        return 0
