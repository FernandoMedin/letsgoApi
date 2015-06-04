from django.db import models


class Users(models.Model):
    facebook_token = models.TextField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Organizations(models.Model):
    user = models.ForeignKey(Users, related_name='orgs')
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    premium = models.BooleanField(default=False)
    premium_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'premium')

    def __unicode__(self):
        return self.name

class Event_Category(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Event_Type(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    place = models.TextField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(Users, blank=True, related_name='user_events', null=True)
    organization = models.ForeignKey(Organizations, blank=True, related_name='org_events', null=True)
    event_type = models.ForeignKey(Event_Type)
    category = models.ForeignKey(Event_Category)

    def __unicode__(self):
        return self.name
