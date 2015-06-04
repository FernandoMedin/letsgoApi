import datetime
from rest_framework import serializers
from app.models import Users, Organizations, Event_Category, Event_Type, Events

class UserSerializer(serializers.ModelSerializer):

    orgs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    user_events = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Users
        read_only_fields = ('created_at', 'updated_at',)
        fields = ('url', 'facebook_token', 'name', 'last_name', 'email', 'orgs',
                  'user_events')

class OrgSerializer(serializers.ModelSerializer):

    org_events = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Organizations
        read_only_fields = ('created_at', 'updated_at', 'premium_at',)
        fields = ('url', 'user', 'name', 'premium', 'org_events')

class Event_Category_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Event_Category
        fields = ('url', 'name')

class Event_Type_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Event_Type
        fields = ('url', 'name')

class Events_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('url', 'name', 'date', 'place', 'time', 'price', 'user',
                  'organization', 'event_type', 'category')


    def validate(self, data):

        if data['date'] < datetime.date.today():
            raise serializers.ValidationError('Invalid data')

        if data['user'] == None and data['organization'] == None:
            raise serializers.ValidationError('An event must be part of an user or an organization')

        return data
