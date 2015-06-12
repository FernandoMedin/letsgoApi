from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from app import views
from rest_framework.authtoken import views as authView
from rest_framework.authtoken.views import obtain_auth_token
from app.social import FaceBook

router = routers.DefaultRouter()
router.register(r'users', views.Profile_ViewSet)
router.register(r'organizations', views.Org_ViewSet)
router.register(r'events', views.Event_ViewSet)
router.register(r'event_category', views.Event_Category_ViewSet)
router.register(r'event_type', views.Event_Type_ViewSet)

urlpatterns = patterns('',

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^auth/facebook/', FaceBook.as_view()),
    url(r'^api-auth/', 'app.token.obtain_expiring_auth_token'),
    url(r'^api-token-auth/', authView.obtain_auth_token),
    url(r'^current/', views.Current.as_view()),
)
