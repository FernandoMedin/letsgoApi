from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from app import views
from app.social import FaceBook

router = routers.DefaultRouter()
router.register(r'users', views.User_ViewSet)
router.register(r'organizations', views.Org_ViewSet)
router.register(r'events', views.Event_ViewSet)
router.register(r'event_category', views.Event_Category_ViewSet)
router.register(r'event_type', views.Event_Type_ViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls)),
    url(r'^auth/facebook/', FaceBook.as_view())
)
