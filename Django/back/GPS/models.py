from django.db import models
from django.contrib.auth.models import User
from Register.models import Device

# Create your models here.
class GPS(models.Model):
    Id_device =  models.ForeignKey(User, on_delete=models.CASCADE)
    Imei = models.CharField(max_length=50, null=False)
    Latitud = models.FloatField()
    Longitud = models.FloatField()
    Fecha = models.DateField()
    Hora = models.DateTimeField()