from django.db import models
from django.utils.translation import gettext_lazy as _
from devices.models import Device

class Sensor(models.Model):
    SENSOR_TYPES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('pressure', 'Pressure'),
        ('light', 'Light'),
        ('motion', 'Motion'),
        ('sound', 'Sound'),
        ('air_quality', 'Air Quality'),
        ('water_level', 'Water Level'),
    ]
    
    SENSOR_STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('error', 'Error'),
        ('calibrating', 'Calibrating'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    current_value = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10, default='')
    status = models.CharField(max_length=20, choices=SENSOR_STATUS, default='active')
    location = models.CharField(max_length=200, blank=True, null=True)
    min_threshold = models.FloatField(blank=True, null=True)
    max_threshold = models.FloatField(blank=True, null=True)
    last_reading = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sensors_tb'
        verbose_name = _('Sensor')
        verbose_name_plural = _('Sensors')
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sensor_readings_tb'
        verbose_name = _('Sensor Reading')
        verbose_name_plural = _('Sensor Readings')
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.sensor.name} - {self.value} at {self.timestamp}"
