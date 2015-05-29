from django.db import models


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    facebook_token = models.TextField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateField()

    def __unicode__(self):
        return self.name


class Organizations(models.Model):
    id_organization = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users')
    name = models.CharField(max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()
    premium = models.BooleanField()
    premium_at = models.DateField()

    def __unicode__(self):
        return self.name


class Event_Category(models.Model):
    id_event_category = models.AutoField(primary_key=True)
    event_category = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Event_Type(models.Model):
    id_event_type = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    place = models.TextField()
    time = models.TimeField()
    price = models.FloatField()
    type = models.ForeignKey('Event_Type')
    category = models.ForeignKey('Event_Category')

    def __unicode__(self):
        return self.name


class Events_Description(models.Model):
    id_description = models.AutoField(primary_key=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name


