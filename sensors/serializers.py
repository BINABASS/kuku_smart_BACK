from rest_framework import serializers
from .models import Sensor, SensorReading

class SensorSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(source='device.name', read_only=True)
    
    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('device_name',)

class SensorReadingSerializer(serializers.ModelSerializer):
    sensor_name = serializers.CharField(source='sensor.name', read_only=True)
    
    class Meta:
        model = SensorReading
        fields = '__all__'
        read_only_fields = ('sensor_name',) 