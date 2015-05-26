from django.views.generic import View
from django.http import HttpResponse
from app.users.users_models import UsersModels

class Users(View):

    def get_token(self, request):
        # Get token from Facebook

        model = UsersModels()

        token = request.POST.get("token", "")
        if token:
            model.insert_token(token)
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

    def auth_user(self, request):
        # Auth users in all requests

        model = UsersModels()

        token = request.POST.get("token", "")

        if token:
            response = "" # Gerar response
            if len(response) != 0:
                return HttpResponse("Autenticado")

            return HttpResponse("Nao autenticado")

        return HttpResponse("Nao autenticado")

    def teste(self, request):
        return "Funfou!!!"
