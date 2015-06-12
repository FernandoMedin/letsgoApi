import datetime
from app.token import TokenAuth
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from app.serializers import ProfileSerializer, UserSerializer, OrgSerializer
from app.models import User, Profile, Organizations, Event_Category, Event_Type, Events
from app.serializers import Events_Serializer, Event_Category_Serializer, Event_Type_Serializer

class Profile_ViewSet(viewsets.ModelViewSet):

    # authentication_classes = (SessionAuthentication, TokenAuth)
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

class Org_ViewSet(viewsets.ModelViewSet):

    queryset = Organizations.objects.all()
    serializer_class = OrgSerializer

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.datetime.now())

class Event_ViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = Events_Serializer

class Event_Category_ViewSet(viewsets.ModelViewSet):
    queryset = Event_Category.objects.all()
    serializer_class = Event_Category_Serializer

class Event_Type_ViewSet(viewsets.ModelViewSet):
    queryset = Event_Type.objects.all()
    serializer_class = Event_Type_Serializer
