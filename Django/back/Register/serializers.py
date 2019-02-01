from rest_framework import serializers
from Register.models import Profile, Device

# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','Address', 'Edad', 'Email', 'Phone', 'User')


# Serializers define the API representation.
class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id','Imei', 'Name', 'Model', 'Date_buy', 'Description')