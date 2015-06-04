import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from app.models import Users, Organizations, Event_Category, Event_Type, Events
from app.serializers import UserSerializer, OrgSerializer
from app.serializers import Events_Serializer, Event_Category_Serializer, Event_Type_Serializer

class User_ViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        """
        Fire before an user is updated
        """
        serializer.save(updated_at=datetime.datetime.now())

class Org_ViewSet(viewsets.ModelViewSet):

    queryset = Organizations.objects.all()
    serializer_class = OrgSerializer

    def perform_update(self, serializer):
        """
        Fire before an organization is updated
        """
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
