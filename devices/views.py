from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Device, DeviceLog
from .serializers import DeviceSerializer, DeviceLogSerializer

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
