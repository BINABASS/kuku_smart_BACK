from rest_framework import serializers
from .models import AnalyticsData, Dashboard, Report, Alert

class AnalyticsDataSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    batch_name = serializers.CharField(source='batch.id', read_only=True)
    
    class Meta:
        model = AnalyticsData
        fields = '__all__'
        read_only_fields = ('farm_name', 'batch_name')

class DashboardSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Dashboard
        fields = '__all__'
        read_only_fields = ('farm_name',)

class ReportSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('farm_name',)

class AlertSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ('farm_name',) 