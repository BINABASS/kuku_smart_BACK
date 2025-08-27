from rest_framework import serializers
from sensors.models import SensorType, Reading
from farms.models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_id', 'name', 'cell_no', 'picture', 'status']

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = '__all__'

class ReadingSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    sensor_type = SensorTypeSerializer(read_only=True)
    
    class Meta:
        model = Reading
        fields = '__all__'
