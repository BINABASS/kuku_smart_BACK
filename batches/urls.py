from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActivityTypeViewSet,
    ActivityScheduleViewSet,
    BatchViewSet,
    BatchActivityViewSet,
    BatchFeedingViewSet
)

router = DefaultRouter()
router.register(r'activity-types', ActivityTypeViewSet)
router.register(r'activity-schedules', ActivityScheduleViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'batch-activities', BatchActivityViewSet)
router.register(r'batch-feedings', BatchFeedingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
