from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreedViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
