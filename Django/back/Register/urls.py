from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import ProfileViewSet, DeviceViewSet


router = routers.DefaultRouter()
router.register(r'/profile', ProfileViewSet)
router.register(r'/device', DeviceViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
