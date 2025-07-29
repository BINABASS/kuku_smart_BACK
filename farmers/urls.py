from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet, FarmViewSet

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet)
router.register(r'farms', FarmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
