from django.views.generic import View
from django.http import HttpResponse


class events_controller(View):

    def create_event(self):
        return 1

    def send_invite(self):
        return 1