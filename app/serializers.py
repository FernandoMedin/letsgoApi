import datetime
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from app.models import PROVIDERS, User, UserManager, Profile, Organizations, Event_Category, Event_Type, Events


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('url', 'facebook_id', 'facebook_token')

class UserSerializer(serializers.ModelSerializer):

    facebook_id = serializers.CharField(
        source='profile.facebook_id',
        allow_null=True,
        read_only=True,
    )

    facebook_token = serializers.CharField(
        source='profile.facebook_token',
        allow_null=True,
        read_only=True,
    )

    orgs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    user_events = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    password = serializers.CharField(
        # input type password
        style={'input_type': 'password'},
        write_only=True,
        allow_null=True,
    )

    token = serializers.CharField(
        source='auth_token',
        read_only=True
    )

    provider = serializers.ChoiceField(choices=PROVIDERS, read_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])

        token, created = Token.objects.get_or_create(user=user)

        return user

    class Meta:
        model = User
        fields = ('url', 'id', 'provider', 'email', 'first_name', 'last_name',
                  'password', 'facebook_id', 'facebook_token',
                  'orgs', 'user_events', 'token')

class OrgSerializer(serializers.ModelSerializer):

    org_events = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Organizations
        read_only_fields = ('created_at', 'updated_at', 'premium_at',)
        fields = ('url', 'id', 'user', 'name', 'premium', 'org_events')

class Event_Category_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Event_Category
        fields = ('url', 'id', 'name')

class Event_Type_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Event_Type
        fields = ('url', 'id', 'name')

class Events_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('url', 'id', 'name', 'date', 'place', 'time', 'price', 'user',
                  'organization', 'event_type', 'category')

    def validate(self, data):

        if data['date'] < datetime.date.today():
            raise serializers.ValidationError('Invalid data')

        if data['user'] == None and data['organization'] == None or \
           data['user'] != None and data['organization'] != None:
            raise serializers.ValidationError('An event must be part of an user or an organization')

        return data
