from django.db import models
from django.contrib.auth.models import User
from Register.models import Device

# Create your models here.
class Cars(models.Model):
    Id_use =  models.ForeignKey(User, on_delete=models.CASCADE)
    Id_device = models.OneToOneField(Device, on_delete=models.CASCADE)
    Imei = models.CharField(max_length=50, null=False)
    Plaque = models.CharField(max_length=255, null=False)
    Model = models.CharField(max_length=10, null=False)
    Price = models.IntegerField()