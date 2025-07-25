from rest_framework import viewsets, permissions
from .models import ActivityType, ActivitySchedule, Batch, BatchActivity, BatchFeeding
from .serializers import (
    ActivityTypeSerializer,
    ActivityScheduleSerializer,
    BatchSerializer,
    BatchActivitySerializer,
    BatchFeedingSerializer
)

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActivityScheduleViewSet(viewsets.ModelViewSet):
    queryset = ActivitySchedule.objects.all()
    serializer_class = ActivityScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticated]

class BatchActivityViewSet(viewsets.ModelViewSet):
    queryset = BatchActivity.objects.all()
    serializer_class = BatchActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

class BatchFeedingViewSet(viewsets.ModelViewSet):
    queryset = BatchFeeding.objects.all()
    serializer_class = BatchFeedingSerializer
    permission_classes = [permissions.IsAuthenticated]
