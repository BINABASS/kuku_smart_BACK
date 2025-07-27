from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import AnalyticsData, Dashboard, Report, Alert
from .serializers import AnalyticsDataSerializer, DashboardSerializer, ReportSerializer, AlertSerializer

# Create your views here.

class AnalyticsDataViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]
