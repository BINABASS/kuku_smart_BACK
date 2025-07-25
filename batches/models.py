from django.db import models
from django.utils.translation import gettext_lazy as _
from farmers.models import Farm

class ActivityType(models.Model):
    activity_type = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'activity_type_tb'
        verbose_name = _('Activity Type')
        verbose_name_plural = _('Activity Types')

class ActivitySchedule(models.Model):
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    activity_description = models.CharField(max_length=300)
    activity_day = models.CharField(max_length=10, default='Day')
    activity_status = models.IntegerField()
    activity_frequency = models.IntegerField()
    
    class Meta:
        db_table = 'activity_schedule_tb'
        verbose_name = _('Activity Schedule')
        verbose_name_plural = _('Activity Schedules')

class Batch(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    breed = models.ForeignKey('breeds.Breed', on_delete=models.CASCADE)
    arrive_date = models.DateField()
    init_age = models.IntegerField()
    harvest_age = models.IntegerField(default=0)
    quantity = models.IntegerField()
    init_weight = models.IntegerField()
    batch_status = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'batches_tb'
        verbose_name = _('Batch')
        verbose_name_plural = _('Batches')

class BatchActivity(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    breed_activity = models.ForeignKey('breeds.BreedActivity', on_delete=models.CASCADE)
    batch_activity_date = models.DateField()
    batch_activity_details = models.CharField(max_length=50)
    batch_activity_cost = models.IntegerField()
    
    class Meta:
        db_table = 'batch_activity_tb'
        verbose_name = _('Batch Activity')
        verbose_name_plural = _('Batch Activities')

class BatchFeeding(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    feeding_date = models.DateField(auto_now_add=True)
    feeding_amount = models.IntegerField()
    status = models.IntegerField()
    
    class Meta:
        db_table = 'batch_feeding_tb'
        verbose_name = _('Batch Feeding')
        verbose_name_plural = _('Batch Feedings')
