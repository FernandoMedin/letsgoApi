from app import views
from app.social import FaceBook
from rest_framework import routers
from django.conf.urls import patterns, include, url
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.Profile_ViewSet)
router.register(r'organizations', views.Org_ViewSet)
router.register(r'events', views.Event_ViewSet)
router.register(r'event_category', views.Event_Category_ViewSet)
router.register(r'event_type', views.Event_Type_ViewSet)

urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^auth/facebook/', FaceBook.as_view()),
    url(r'^api-auth/', 'app.token.obtain_auth_token'),
    url(r'^current/', views.Current.as_view()),
)
