from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Sensor, SensorReading
from .serializers import SensorSerializer, SensorReadingSerializer

# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]

class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    permission_classes = [permissions.IsAuthenticated]
