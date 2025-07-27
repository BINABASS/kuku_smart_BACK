from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsDataViewSet, DashboardViewSet, ReportViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'analytics/data', AnalyticsDataViewSet)
router.register(r'analytics/dashboards', DashboardViewSet)
router.register(r'analytics/reports', ReportViewSet)
router.register(r'analytics/alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 