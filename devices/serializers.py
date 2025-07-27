from rest_framework import serializers
from .models import Device, DeviceLog

class DeviceSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('farm_name',)

class DeviceLogSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)
    
    class Meta:
        model = DeviceLog
        fields = '__all__'
        read_only_fields = ('device_name',) 