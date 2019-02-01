from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets
from .views import CarsViewSet


router = routers.DefaultRouter()
router.register(r'', CarsViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
