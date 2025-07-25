from django.db import models
from django.utils.translation import gettext_lazy as _

class Breed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'breeds_tb'
        verbose_name = _('Breed')
        verbose_name_plural = _('Breeds')

class BreedActivity(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    activity_type = models.ForeignKey('batches.ActivityType', on_delete=models.CASCADE)
    age = models.IntegerField()
    breed_activity_status = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'breed_activities_tb'
        verbose_name = _('Breed Activity')
        verbose_name_plural = _('Breed Activities')

class BreedCondition(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    condition_min = models.IntegerField()
    condition_max = models.IntegerField()
    condition_status = models.IntegerField(default=1)
    condition_type = models.ForeignKey('ConditionType', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'breed_conditions'
        verbose_name = _('Breed Condition')
        verbose_name_plural = _('Breed Conditions')

class BreedFeeding(models.Model):
    quantity = models.IntegerField(default=0)
    breed_feed_status = models.IntegerField(default=1)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    food_type = models.ForeignKey('FoodType', on_delete=models.CASCADE)
    age = models.IntegerField()
    frequency = models.IntegerField()
    
    class Meta:
        db_table = 'breed_feeding_tb'
        verbose_name = _('Breed Feeding')
        verbose_name_plural = _('Breed Feedings')

class ConditionType(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'condition_types_tb'
        verbose_name = _('Condition Type')
        verbose_name_plural = _('Condition Types')

class FoodType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'food_types_tb'
        verbose_name = _('Food Type')
        verbose_name_plural = _('Food Types')
