from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from Register.serializers import ProfileSerializer, DeviceSerializer
from Register.models import Profile, Device

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
