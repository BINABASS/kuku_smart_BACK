from django.shortcuts import render
from rest_framework import viewsets, permissions
from sensors.models import SensorType, Reading
from sensors.serializers import SensorTypeSerializer, ReadingSerializer

# Create your views here.

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().select_related('device', 'sensor_type')
    serializer_class = ReadingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        device_id = self.request.query_params.get('device')
        sensor_type_id = self.request.query_params.get('sensor_type')
        from_ts = self.request.query_params.get('from')
        to_ts = self.request.query_params.get('to')

        if device_id:
            qs = qs.filter(device_id=device_id)
        if sensor_type_id:
            qs = qs.filter(sensor_type_id=sensor_type_id)
        if from_ts:
            qs = qs.filter(timestamp__gte=from_ts)
        if to_ts:
            qs = qs.filter(timestamp__lte=to_ts)
        return qs.order_by('-timestamp')
