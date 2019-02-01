from django.db import models
from Profile.models import Profile

# Create your models here.

class Device(models.Model):
    Imei = models.CharField(max_length=50, null=False)
    Name = models.CharField(max_length=50, null=False)
    Model = models.CharField(max_length=50, null=False)
    Date_buy = models.CharField(max_length=50, null=False)
    Description= models.CharField(max_length=50, null=True)
