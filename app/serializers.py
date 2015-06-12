import datetime
from rest_framework import serializers
from app.models import User, Profile, Organizations, Event_Category, Event_Type, Events


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('url', 'facebook_id', 'facebook_token')


class UserSerializer(serializers.ModelSerializer):

    facebook_id    = serializers.CharField(
        source='profile.facebook_id',
        allow_null=True,
        # read_only=True
    )

    facebook_token = serializers.CharField(
        source='profile.facebook_token',
        allow_null=True,
        # read_only=True
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

    class Meta:
        model = User
        fields = ('url', 'email', 'facebook_id',
                  'facebook_token', 'orgs', 'user_events')

    def create(self, validated_data):

        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(owner=user, **profile_data)
        return user

    def update(self, instance, validated_data):

        # instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile_data = validated_data.pop('profile')
        profile = Profile(
            owner=instance,
            facebook_id    = profile_data.get('facebook_id'),
            facebook_token = profile_data.get('facebook_token')
        )
        profile.save()

        return instance

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

        if data['user'] == None and data['organization'] == None or \
           data['user'] != None and data['organization'] != None:
            raise serializers.ValidationError('An event must be part of an user or an organization')

        return data
