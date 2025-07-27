from django.db import models
from django.utils.translation import gettext_lazy as _
from farmers.models import Farm

class Device(models.Model):
    DEVICE_TYPES = [
        ('sensor', 'Sensor'),
        ('controller', 'Controller'),
        ('monitor', 'Monitor'),
        ('gateway', 'Gateway'),
    ]
    
    DEVICE_STATUS = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('maintenance', 'Maintenance'),
        ('error', 'Error'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS, default='offline')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    firmware_version = models.CharField(max_length=20, default='1.0.0')
    last_seen = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'devices_tb'
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class DeviceLog(models.Model):
    LOG_LEVELS = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('critical', 'Critical'),
    ]
    
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=LOG_LEVELS)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'device_logs_tb'
        verbose_name = _('Device Log')
        verbose_name_plural = _('Device Logs')
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.device.name} - {self.level} - {self.timestamp}"
