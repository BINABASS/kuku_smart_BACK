from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, SensorReadingViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'sensor-readings', SensorReadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 