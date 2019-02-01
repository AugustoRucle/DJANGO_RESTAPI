from rest_framework import serializers
from .models import Cars

# Serializers define the API representation.
class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ('Id_use','Id_device', 'Imei', 'Plaque', 'Model', 'Price')
