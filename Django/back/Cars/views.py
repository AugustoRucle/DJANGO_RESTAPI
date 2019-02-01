from django.shortcuts import render
from .models import Cars
from rest_framework import routers, serializers, viewsets
from .serializers import CarsSerializer

# Create your views here.
class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
