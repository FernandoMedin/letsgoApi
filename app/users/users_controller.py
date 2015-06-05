from django.views.generic import View
from django.http import HttpResponse
from app.users.users_models import UsersModels


class Users(View):

    def create_user(self, request):
        # Get token from Facebook and create an user

        model = UsersModels()

        token = request.POST.get("token", "")
        name = request.POST.get("name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        if token:
            model.insert_token(token, name, last_name, email)
            return HttpResponse("Foi")

        return HttpResponse("Nao foi")

    def login(self, request):
        # Login with Facebook token

        model = UsersModels()

        token = request.POST.get("token", "")
        if token:
            response = model.login_facebook(token)
            if response:
                return HttpResponse("Logado")

            return HttpResponse("Sem login")

        return HttpResponse("Sem token")

    def create_token(self):
        return 1

    def auth_user(self, request):
        # Auth users in all requests

        model = UsersModels()

        token = request.POST.get("token", "")

        if token:
            response = "" # Generate response
            if len(response) != 0:
                return HttpResponse("Autenticado")

            return HttpResponse("Nao autenticado")

        return HttpResponse("Nao autenticado")

    def teste(self, request):
        return "Funfou!!!"
