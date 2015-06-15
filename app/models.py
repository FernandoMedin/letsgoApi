from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

PROVIDERS = ( ('Local', 'Local'), ('Facebook', 'Facebook') )

class UserManager(BaseUserManager):
    # Copied for the win https://thinkster.io/django-angularjs-tutorial/
    def create_user(self, email, password=None, first_name=None, last_name=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        user = self.model(email = self.normalize_email(email))
        if password:
            user.set_password(password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return user

    # used with python manage.py createsuperuser
    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.save()

        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name  = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    provider   = models.CharField(choices=PROVIDERS, default="Local", max_length=15)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

class Profile(models.Model):
    owner = models.OneToOneField(User, primary_key=True)
    facebook_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    facebook_token = models.CharField(max_length=1000, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.owner.email

class Organizations(models.Model):
    user = models.ForeignKey(User, related_name='orgs')
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
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
    description = models.TextField(default="")
    date = models.DateField()
    place = models.TextField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, blank=True, related_name='user_events', null=True)
    organization = models.ForeignKey(Organizations, blank=True, related_name='org_events', null=True)
    event_type = models.ForeignKey(Event_Type)
    category = models.ForeignKey(Event_Category)

    def __unicode__(self):
        return self.name
