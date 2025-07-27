from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, DeviceLogViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'device-logs', DeviceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 