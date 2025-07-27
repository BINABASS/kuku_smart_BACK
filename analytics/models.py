from django.db import models
from django.utils.translation import gettext_lazy as _
from farmers.models import Farm
from batches.models import Batch

class AnalyticsData(models.Model):
    DATA_TYPES = [
        ('production', 'Production'),
        ('health', 'Health'),
        ('financial', 'Financial'),
        ('environmental', 'Environmental'),
        ('performance', 'Performance'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    data_type = models.CharField(max_length=20, choices=DATA_TYPES)
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'analytics_data_tb'
        verbose_name = _('Analytics Data')
        verbose_name_plural = _('Analytics Data')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.farm.name} - {self.metric_name} - {self.value}"

class Dashboard(models.Model):
    DASHBOARD_TYPES = [
        ('production', 'Production'),
        ('financial', 'Financial'),
        ('health', 'Health'),
        ('overview', 'Overview'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DASHBOARD_TYPES)
    configuration = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'analytics_dashboards_tb'
        verbose_name = _('Dashboard')
        verbose_name_plural = _('Dashboards')
    
    def __str__(self):
        return f"{self.farm.name} - {self.name}"

class Report(models.Model):
    REPORT_TYPES = [
        ('production', 'Production Report'),
        ('financial', 'Financial Report'),
        ('health', 'Health Report'),
        ('inventory', 'Inventory Report'),
        ('custom', 'Custom Report'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=REPORT_TYPES)
    parameters = models.JSONField(default=dict)
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        db_table = 'analytics_reports_tb'
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')
        ordering = ['-generated_at']
    
    def __str__(self):
        return f"{self.farm.name} - {self.name}"

class Alert(models.Model):
    ALERT_TYPES = [
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('info', 'Info'),
        ('success', 'Success'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ALERT_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'analytics_alerts_tb'
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.farm.name} - {self.title}"
