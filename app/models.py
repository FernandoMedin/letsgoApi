from django.db import models


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    facebook_token = models.TextField()
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


